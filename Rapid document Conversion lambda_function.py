import boto3
import json
import urllib.parse

s3_client = boto3.client('s3')
textract_client = boto3.client('textract')
dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('ExtractedTextTable')

def lambda_handler(event, context):
    try:
        print("Received Event: ", json.dumps(event))

        # Handle S3-triggered event (when a file is uploaded to S3)
        if 'Records' in event:
            bucket_name = event['Records'][0]['s3']['bucket']['name']
            file_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

        # Handle API Gateway request (manual request via Postman/cURL)
        elif 'bucket_name' in event and 'file_key' in event:
            bucket_name = event['bucket_name']
            file_key = event['file_key']

        else:
            print("Invalid event structure")
            return {
                'statusCode': 400,
                'body': json.dumps("Invalid event structure. Expected S3 event notification or API request.")
            }

        print(f"Processing file: {file_key} from bucket: {bucket_name}")

        # Validate supported formats
        allowed_formats = ('.pdf', '.png', '.jpeg', '.jpg', '.tiff')
        if not file_key.lower().endswith(allowed_formats):
            return {
                'statusCode': 400,
                'body': json.dumps("Error: Unsupported file format. Please upload a PDF, JPEG, PNG, or TIFF.")
            }

        # Ensure object exists in S3
        try:
            s3_client.head_object(Bucket=bucket_name, Key=file_key)
        except Exception as e:
            print("Error: S3 object not found", str(e))
            return {
                'statusCode': 400,
                'body': json.dumps(f"Error: S3 object not found: {str(e)}")
            }

        # Call Amazon Textract to extract text
        response = textract_client.analyze_document(
            Document={'S3Object': {'Bucket': bucket_name, 'Name': file_key}},
            FeatureTypes=['TABLES', 'FORMS']
        )

        # Extract the detected text
        extracted_text = "\n".join(
            block['Text'] for block in response['Blocks'] if block['BlockType'] == 'LINE'
        )

        print("Extracted Text: ", extracted_text)

        # Store extracted text in DynamoDB
        table.put_item(
            Item={
                'document_name': file_key,
                'extracted_text': extracted_text
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps(f"Text extracted and stored successfully for {file_key}")
        }

    except Exception as e:
        print("Error: ", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error processing file: {str(e)}")
        }

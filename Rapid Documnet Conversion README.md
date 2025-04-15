
# Rapid Document Conversion using AWS

This project automates document text extraction using AWS. Users upload files to Amazon S3, and AWS Lambda triggers Amazon Textract to extract text, which is stored in DynamoDB.

## Project Goals

- Automate document text extraction using AWS Textract.
- Store extracted text in DynamoDB for easy access.
- Provide a REST API (via API Gateway) to retrieve processed text.
- Ensure scalability and security using AWS Lambda, IAM, and API Gateway API Keys.

## AWS Services Used

- Amazon S3 :-	Stores uploaded documents (PDFs, images).
- AWS Lambda :- Extracts text from documents using AWS Textract.
- Amazon Textract :- Performs OCR (Optical Character Recognition) on PDFs and images.
- Amazon DynamoDB :- Stores extracted text for retrieval.
- Amazon API Gateway :-	Provides a REST API to access extracted text.
- AWS CloudWatch :-	Logs API calls, Lambda executions, and errors.
- AWS IAM :- Manages permissions for Lambda, Textract, and API Gateway.

## Workflow

### Step 1: Upload a Document to S3
The user uploads a PDF, PNG, or JPEG document to an Amazon S3 bucket (rapid-documents-bucket).
### Step 2: AWS Lambda is Triggered
When a file is uploaded to S3, an S3 Event Notification triggers an AWS Lambda function (doc-processor-lambda).
The function reads the uploaded file details (bucket name, file name).
### Step 3: AWS Textract Extracts Text
The Lambda function calls Amazon Textract to process the document.
Textract extracts text and form data from the document.
### Step 4: Store Extracted Text in DynamoDB
The Lambda function stores the extracted text in an Amazon DynamoDB table (ExtractedTextTable).
This allows quick retrieval of extracted data.
### Step 5: Access Extracted Text via API Gateway
Users can call an API endpoint (provided by API Gateway) to retrieve processed text.
The API requires an API Key for security.
### Step 6: Monitor and Manage Logs
AWS CloudWatch logs Lambda executions and API requests for monitoring and debugging.

## API Usage
POST :- https://4wtabtdhp0.execute-api.ap-south-1.amazonaws.com/prod

json

{

  "bucket_name": "rapid-documents-bucket",

  "file_key": "f72162fbab07a4452b499550ab9f9be3.jpg"

}

## Endpoint
x-api-key :- "Replace with your API key".


## Visual Representation of the Project Workflow

User → Uploads Document → [S3 Bucket] → Triggers [Lambda Function] → Calls [Amazon Textract] → Stores in [DynamoDB] → Accessible via [API Gateway] → User Retrieves Extracted Text


## Conclusion

The Rapid Document Conversion using AWS project successfully automates text extraction from documents using cloud services. By leveraging Amazon S3, AWS Lambda, Amazon Textract, DynamoDB, and API Gateway, we created a scalable, serverless solution for processing documents in real time.

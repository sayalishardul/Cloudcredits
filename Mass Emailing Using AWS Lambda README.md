
# Mass Emailing using AWS Lambda

This project demonstrates how to automate sending mass emails using AWS Lambda and Amazon SES (Simple Email Service). The solution is serverless, reducing infrastructure costs while ensuring reliable email delivery.

We use AWS Lambda to trigger an email-sending function that utilizes Amazon SES to send bulk emails efficiently.

## Project Goal

- To implement an automated mass emailing system using AWS Lambda and Amazon Simple Email Service (SES). This allows us to send bulk emails efficiently, without managing servers.



## AWS Services Used

- AWS Lambda :- Runs the email-sending function serverlessly
- Amazon SES :- Handles email sending with verified sender authentication
- IAM (Identity & Access Management) :-	Manages permissions for Lambda to use SES.

## Workflow

### Step 1 : Setting Up Amazon SES
- Go to AWS Console → Amazon SES → Verified Identities.
- Verify an email address (AWS requires this before sending emails).
- If needed, request SES production access to send emails to unverified recipients.
### Step 2 : Creating the AWS Lambda Function
- Go to AWS Lambda → Create Function → Author from Scratch.
- Choose Python (latest version) as the runtime.
- Create a new IAM role and attach the AmazonSESFullAccess policy.
- Deploy the Lambda function (explained below).
### Step 3 : Writing the Lambda Function (Python Code)
- The function initializes an SES client and sends emails using the send_email() method.
- It takes a list of recipient emails and sends a formatted message.
- This function authenticates SES, sets up email recipients, and sends messages.
### Step 4 : Assigning Permissions to Lambda
- In AWS IAM, attach AmazonSESFullAccess to the Lambda function role.
### Step 5 : Testing the Function
- Click Test in AWS Lambda.
- If successful, the recipients will receive an email.


## Conclusion

This project demonstrates how to send bulk emails efficiently using AWS Lambda and SES. By automating email notifications, businesses can improve customer engagement without managing servers.
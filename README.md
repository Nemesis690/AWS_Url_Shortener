# AWS URL Shortener

This is a serverless URL shortener built using AWS Lambda, API Gateway, and DynamoDB. It allows you to create short URLs and redirect users to the original long URLs.

## Features
- Generate short URLs for any given long URL.
- Redirect users from a short URL to the original URL.
- Automatically handle scaling and availability using AWS services.

## Architecture
- **AWS Lambda**: Backend logic for creating and redirecting URLs.
- **API Gateway**: Exposes REST APIs to interact with the Lambda functions.
- **DynamoDB**: Stores the mapping between short codes and long URLs.
## Setup
Set Up AWS Resources
# Create the DynamoDB Table

Go to the AWS Management Console and open the DynamoDB service.

Click on "Create table."

Set the table name to UrlShortener (case-sensitive).

Set the partition key to shortCode (String).

Leave other settings as default and create the table.

# Deploy the Lambda Functions

Open the AWS Lambda console.

Create a new Lambda function named create_url using the Python 3.9 runtime.

Upload the create_url/lambda_function.py code to this function.

Create another Lambda function named redirect_url and upload the redirect_url/lambda_function.py code.

Make sure both Lambda functions have the necessary IAM role permissions to access DynamoDB. You can attach the AmazonDynamoDBFullAccess policy for simplicity.

# Set Up API Gateway

Open the Amazon API Gateway console.

Create a new REST API.

Create a resource named /shorten and set up a POST method that triggers the create_url Lambda.

Create a {proxy+} resource to handle all other paths and set up a GET method that triggers the redirect_url Lambda.

Deploy your API and note the invoke URL.

# Update Lambda Environment Variables (Optional)

If you want to store the API URL or table name as environment variables in Lambda, you can do that in the Lambda console under the “Configuration” tab.

# Test the Setup

Use a tool like Postman to send a POST request to your /shorten endpoint with a JSON body containing a longUrl.

Then test the generated short URL in your browser to ensure it redirects correctly.

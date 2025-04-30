import json
import boto3
import urllib.parse

# Initialize AWS clients
s3 = boto3.client('s3')
sns = boto3.client('sns')

SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:311141518894:lamda_learning'

def lambda_handler(event, context):
    try:
        # Extract bucket and key
        record = event['Records'][0]
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')

        # Get the object content
        obj = s3.get_object(Bucket=bucket, Key=key)
        content = obj['Body'].read().decode('utf-8', errors='ignore')

        # Check for 'error' in content
        if 'error' in content.lower():
            message = f"⚠️ 'error' found in uploaded file: {key}\n\nPreview:\n{content[:300]}"
            subject = "Alert: 'Error' Detected in Uploaded File"
            send_sns_notification(message, subject)

        return {
            'statusCode': 200,
            'body': json.dumps(f"File {key} processed.")
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Log any error for debugging
        return {
            'statusCode': 500,
            'body': json.dumps(f"Failed to process file: {str(e)}")
        }

def send_sns_notification(message, subject):
    try:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject=subject
        )
        print(f"Message sent to SNS: {message}")  # Log successful SNS send
    except Exception as e:
        print(f"Failed to send SNS message: {str(e)}")  # Log error if SNS send fails

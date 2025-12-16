import json
import boto3
import string
import random
import time
import re

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("UrlShortener")

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def is_valid_url(url):
    pattern = re.compile(
        r'^(https?|ftp)://[^\s/$.?#].[^\s]*$',
        re.IGNORECASE
    )
    return re.match(pattern, url) is not None

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    long_url = body.get("longUrl")

    if not long_url or not is_valid_url(long_url):
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid URL"})
        }

    short_code = generate_short_code()

    expiry_days = body.get("expiryDays", 7)
    expiry_time = int(time.time()) + expiry_days * 86400

    table.put_item(
        Item={
            "shortCode": short_code,
            "longUrl": long_url,
            "createdAt": int(time.time()),
            "expiryTime": expiry_time,
            "clickCount": 0
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "shortCode": short_code
        })
    }

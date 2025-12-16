import boto3
import time

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("UrlShortener")

def lambda_handler(event, context):
    short_code = event["pathParameters"]["proxy"]

    response = table.get_item(
        Key={"shortCode": short_code}
    )

    if "Item" not in response:
        return {
            "statusCode": 404,
            "body": "Short URL not found"
        }

    item = response["Item"]

    if item["expiryTime"] < int(time.time()):
        return {
            "statusCode": 410,
            "body": "Short URL expired"
        }

    table.update_item(
        Key={"shortCode": short_code},
        UpdateExpression="SET clickCount = clickCount + :inc",
        ExpressionAttributeValues={":inc": 1}
    )

    return {
        "statusCode": 302,
        "headers": {
            "Location": item["longUrl"]
        }
    }

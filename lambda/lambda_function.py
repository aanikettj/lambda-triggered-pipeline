import urllib3
import base64
import json

def lambda_handler(event, context):

    jenkins_url = "http://18.212.86.180:8080/job/s3-lambda-jenkins-cicd/build"

    username = "your-jenkins-username"
    api_token = "your-api-token"

    auth = base64.b64encode(
        f"{username}:{api_token}".encode()
    ).decode()

    headers = {
        "Authorization": f"Basic {auth}"
    }

    http = urllib3.PoolManager()

    response = http.request(
        "POST",
        jenkins_url,
        headers=headers
    )

    return {
        "statusCode": response.status,
        "body": "Jenkins pipeline triggered successfully"
    }


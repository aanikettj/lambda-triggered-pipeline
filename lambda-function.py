import urllib3
import base64

def lambda_handler(event, context):

    jenkins_url = "http://18.212.86.180:8080/job/lambda-triggered-pipeline/build"

    username = "admin"
    api_token = "112f3b4130fad0573d107ef75d3e49313a"

    auth = base64.b64encode(f"{username}:{api_token}".encode()).decode()

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

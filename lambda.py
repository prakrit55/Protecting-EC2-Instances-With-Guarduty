import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    try:
        res = json.dumps(event)
        resource_dict = json.loads(res)
        resource_id = resource_dict["detail"]["findings"][0]["Resources"][0]["Id"]
        instance_id = resource_id.split("/")[-1]
        print("instance_id",instance_id)
        ec2 = boto3.client('ec2')
        response = ec2.stop_instances(InstanceIds=[instance_id])
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Successfully processed Security Hub event",
                "instance_ids": instance_ids
            })
        }
    except Exception as e:
        print(f"Error processing event: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Error processing Security Hub event",
                "error": str(e)
            })
        }
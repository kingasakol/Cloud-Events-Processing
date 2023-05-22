from cloudevents.http import CloudEvent
from ..gcp.cloud_function_wrapper import CloudFunctionWrapper

def lambda_handler(event, context):
    attributes = {
        "type": "image",
        "source": "aws.lambda",
    }
    data = event

    cloudevent = CloudEvent(attributes, data)
    CloudFunctionWrapper().publish_message(cloudevent)

    return {"statusCode": 200}
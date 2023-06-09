from cloudevents.http import CloudEvent
from cloud_function_wrapper import CloudFunctionWrapper

def lambda_handler(event, context):
    attributes = {
        "type": "image",
        "source": "aws.lambda",
    }

    cloudevent = CloudEvent(attributes, event)
    
    return CloudFunctionWrapper().publish_message(cloudevent)
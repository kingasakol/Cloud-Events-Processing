from cloudevents.http import CloudEvent
from cloud_function_wrapper import CloudFunctionWrapper


attributes = {
    "type": "image",
    "source": "aws.lambda",
}
data = 'TEST'
cloudevent = CloudEvent(attributes, data)
print(CloudFunctionWrapper().publish_message(cloudevent))

from cloudevents.http import CloudEvent, to_structured
from config import EVENT_URL
import os
import requests


def lambda_handler(event, context):
    attributes = {
        "type": "image",
        "source": "aws.lambda",
    }
    data = event

    cloudevent = CloudEvent(attributes, data)
    headers, body = to_structured(cloudevent)

    requests.post(EVENT_URL, data=body, headers=headers)

    return {"statusCode": 200}
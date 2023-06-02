import os
from cloudevents.http import CloudEvent
from google.pubsub import PublisherClient, PublishRequest, PubsubMessage
from config import GCP_PROJECT_NAME, GCP_CREDS_PATH, GCP_TOPIC
import os


class CloudFunctionWrapper:
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.dirname(
            os.path.abspath(__file__)) + "/" + GCP_CREDS_PATH
        self.publisher = PublisherClient()

    def publish_message(self, event: CloudEvent):
        topic_path = self.publisher.topic_path(GCP_PROJECT_NAME, GCP_TOPIC)
        request = PublishRequest(topic=topic_path, messages=[
            PubsubMessage(data=event.data["payload"].encode('utf-8'), attributes=event.get_attributes())])
        self.publisher.publish(request)
        return

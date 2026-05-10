import boto3
from core.ports import IEventClient


class AwsSnsClient(IEventClient):
    def __init__(self, topic_arn: str, region: str = "us-east-1") -> None:
        self._topic_arn = topic_arn
        self._sns = boto3.client("sns", region_name=region)

    def publish(self, item_id: str, event_type: str) -> None:
        self._sns.publish(
            TopicArn=self._topic_arn,
            Message=item_id,
            Subject=event_type,
        )

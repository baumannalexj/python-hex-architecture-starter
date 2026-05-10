from unittest.mock import MagicMock, patch
from clients.aws_sns import AwsSnsClient


def test_publish_calls_sns():
    with patch("clients.aws_sns.boto3.client") as mock_boto:
        mock_sns = MagicMock()
        mock_boto.return_value = mock_sns

        client = AwsSnsClient(topic_arn="arn:aws:sns:us-east-1:123456789012:test-topic")
        client.publish("item-42", "item.created")

        mock_sns.publish.assert_called_once_with(
            TopicArn="arn:aws:sns:us-east-1:123456789012:test-topic",
            Message="item-42",
            Subject="item.created",
        )

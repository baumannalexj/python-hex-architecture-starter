from unittest.mock import patch, MagicMock

import pytest
from clients.aws_sns import AwsSnsClient

topic_arn = "fake-topic"
region = "fake-east-1"


@pytest.fixture(autouse=True)
def mock_boto_sns():
    return MagicMock()


@pytest.fixture(autouse=True)
def aws_sns(mock_boto_sns):
    with patch("boto3.client") as mock_client:
        mock_client.return_value = mock_boto_sns
        return AwsSnsClient(topic_arn, region)


def test_publish_calls_sns(aws_sns, mock_boto_sns):
    item_id = "item-42"
    event_type = "item.created"

    mock_boto_sns.publish.return_value = None

    aws_sns.publish(item_id, event_type)

    mock_boto_sns.publish.assert_called_once_with(
        TopicArn=topic_arn,
        Message=item_id,
        Subject=event_type,
    )

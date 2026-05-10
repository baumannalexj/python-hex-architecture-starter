from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sns_topic_arn: str = "arn:aws:sns:us-east-1:000000000000:local-topic"
    aws_region: str = "us-east-1"

    model_config = {"env_prefix": "APP_"}

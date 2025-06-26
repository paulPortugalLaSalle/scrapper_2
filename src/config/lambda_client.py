from os import environ

import boto3
from boto3_type_annotations.lambda_ import Client
from dotenv import load_dotenv

load_dotenv()

lambda_client: Client = boto3.client(
    "lambda",
    aws_access_key_id=environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name=environ.get("REGION", "us-west-2"),
)

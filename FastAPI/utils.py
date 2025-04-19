# everything needed for AWS s3, RDS, etc.

from sqlalchemy import create_engine
import boto3

def get_db():
    engine = create_engine("sqlite:///./test.db")
    return engine

def get_s3_client():
    config = Config(
        region_name="us-east-1",
        signature_version="s3v4",
        s3={"signature_version": "s3v4"},
    )
    client = boto3.client("s3", config=config)
    return client

    
    
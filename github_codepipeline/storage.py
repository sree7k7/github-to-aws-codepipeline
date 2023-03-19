import aws_cdk as cdk
from aws_cdk import aws_iam as iam
from constructs import Construct
from aws_cdk import (
    Stack,
)
from aws_cdk import aws_s3 as s3

class Storage(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.dnac_bucket = s3.Bucket(
            self,
            "Bucket",
            access_control = s3.BucketAccessControl.PRIVATE,
            encryption = s3.BucketEncryption.S3_MANAGED,
            versioned = True,
            block_public_access = s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )

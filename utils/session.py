import boto3
from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

from config import DEFAULT_REGION


class AWSSession:
    """Handles boto3 session creation and AWS identity lookup."""

    def __init__(self, region: str = DEFAULT_REGION):
        self.region = region
        self.session = boto3.Session(region_name=region)

    def client(self, service: str):
        """Return a boto3 client for a given AWS service."""
        return self.session.client(service)

    def get_identity(self):
        """
        Return AWS account identity.
        Used to verify credentials before inventory collection.
        """
        try:
            sts = self.client("sts")
            return sts.get_caller_identity()

        except NoCredentialsError:
            raise RuntimeError(
                "AWS credentials not found. Run 'aws configure' or login with AWS SSO."
            )

        except (ClientError, BotoCoreError) as err:
            raise RuntimeError(f"Unable to authenticate with AWS: {err}")
from utils.session import AWSSession
from utils.tags import get_name_tag


class EC2Collector:
    """Collect EC2 instance inventory."""

    def __init__(self, region: str):
        self.region = region
        self.client = AWSSession(region).client("ec2")

    def collect(self) -> list[dict]:
        """Fetch EC2 inventory for a region."""
        inventory = []

        paginator = self.client.get_paginator("describe_instances")

        for page in paginator.paginate():
            for reservation in page.get("Reservations", []):
                for instance in reservation.get("Instances", []):

                    inventory.append({
                        "Region": self.region,
                        "Instance Name": get_name_tag(instance.get("Tags")),
                        "Instance ID": instance.get("InstanceId"),
                        "State": instance["State"]["Name"],
                        "Instance Type": instance.get("InstanceType"),
                        "Private IP": instance.get("PrivateIpAddress", "-"),
                        "Public IP": instance.get("PublicIpAddress", "-"),
                        "Platform": instance.get("Platform", "Linux/Unix"),
                        "Availability Zone": instance["Placement"]["AvailabilityZone"],
                        "Launch Time": instance["LaunchTime"].strftime(
                            "%Y-%m-%d %H:%M:%S UTC"
                        ),
                    })

        return inventory
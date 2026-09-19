from utils.session import AWSSession


class EBSCollector:
    """Collect EBS volume inventory."""

    def __init__(self, region: str):
        self.region = region
        self.client = AWSSession(region).client("ec2")

    def collect(self) -> list[dict]:
        """Fetch EBS volume inventory for a region."""
        inventory = []

        paginator = self.client.get_paginator("describe_volumes")

        for page in paginator.paginate():
            for volume in page.get("Volumes", []):

                attachments = volume.get("Attachments", [])

                inventory.append({
                    "Region": self.region,
                    "Volume ID": volume.get("VolumeId"),
                    "State": volume.get("State"),
                    "Size (GiB)": volume.get("Size"),
                    "Volume Type": volume.get("VolumeType"),
                    "Encrypted": volume.get("Encrypted"),
                    "Availability Zone": volume.get("AvailabilityZone"),
                    "IOPS": volume.get("Iops", "-"),
                    "Throughput (MiB/s)": volume.get("Throughput", "-"),
                    "Snapshot ID": volume.get("SnapshotId", "-"),
                    "Attached Instance": (
                        attachments[0].get("InstanceId")
                        if attachments else "-"
                    ),
                    "Device": (
                        attachments[0].get("Device")
                        if attachments else "-"
                    ),
                    "Created Time": volume["CreateTime"].strftime(
                        "%Y-%m-%d %H:%M:%S UTC"
                    ),
                })

        return inventory
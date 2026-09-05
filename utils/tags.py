from typing import Dict, List


def tags_to_dict(tags: List[dict] | None) -> Dict[str, str]:

    if not tags:
        return {}

    return {
        tag["Key"]: tag["Value"]
        for tag in tags
        if "Key" in tag and "Value" in tag
    }


def get_name_tag(tags: List[dict] | None) -> str:

    return tags_to_dict(tags).get("Name", "-")
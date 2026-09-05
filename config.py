from pathlib import Path
from datetime import datetime

APP_NAME = "aws-cloud-inventory"
APP_VERSION = "1.0.0"

# Default AWS region
DEFAULT_REGION = "ap-south-1"

# Output folder
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

# Default report name
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
DEFAULT_REPORT = OUTPUT_DIR / f"cloudinventory_{TIMESTAMP}.xlsx"
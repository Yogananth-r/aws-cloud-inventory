# AWS Cloud Inventory

A lightweight Python CLI tool that runs directly inside **AWS CloudShell** to collect AWS infrastructure inventory and export it into a professionally formatted Excel workbook.

## Why AWS CloudShell?

* Runs inside your AWS account.
* Uses the CloudShell IAM identity automatically.
* No access keys or `aws configure` required.
* No local setup needed after installation.

## Features (V1)

* Collect EC2 inventory from an AWS region.
* Export inventory to an Excel (`.xlsx`) report.
* Styled Excel output with filters, frozen headers, and auto-sized columns.
* Built using Boto3, Rich, Typer, and OpenPyXL.

## Project Structure

```text id="pj0psb"
aws-cloud-inventory/
├── cli.py
├── config.py
├── collectors/
│   └── ec2.py
├── exporter/
│   └── excel.py
├── utils/
│   ├── session.py
│   └── tags.py
├── requirements.txt
└── README.md
```

## Installation in AWS CloudShell

Clone the repository:

```bash id="y4ukkw"
git clone git@github.com:<your-github-username>/aws-cloud-inventory.git
cd aws-cloud-inventory
```

Install dependencies:

```bash id="epdd9a"
pip3 install -r requirements.txt
```

> AWS CloudShell already provides Python and AWS credentials through the active IAM session.

## Usage

Display help:

```bash id="kyr1wf"
python3 cli.py --help
```

Show version:

```bash id="s26nyy"
python3 cli.py version
```

Export EC2 inventory for the current region:

```bash id="vrlbxg"
python3 cli.py export
```

Export EC2 inventory for a specific region:

```bash id="onwsxw"
python3 cli.py export --region eu-central-1
```

## Output

The generated Excel report is saved in the `output/` directory.

Example:

```text id="hzlz9a"
output/
└── aws-cloud-inventory_20260905_103015.xlsx
```

The workbook currently contains:

| Worksheet     | Description                                        |
| ------------- | -------------------------------------------------- |
| EC2 Inventory | EC2 instance metadata for the selected AWS region. |

### Included EC2 Fields

* Instance Name
* Instance ID
* Region
* State
* Instance Type
* Private IP
* Public IP
* Platform
* Availability Zone
* Launch Time

## Roadmap

### V0.2

* Multi-region EC2 inventory (`--all-regions`).

### V0.3

* RDS inventory.
* EBS inventory.
* S3 inventory.

### V0.4

* IAM inventory.
* VPC/Subnet inventory.
* Load Balancer inventory.

### V1.0

* Complete AWS account inventory.
* Summary worksheet with resource counts.
* Security and configuration insights.
* Installable CloudShell CLI (`aws-cloud-inventory` command).

## Tech Stack

* Python
* Boto3
* Typer
* Rich
* OpenPyXL
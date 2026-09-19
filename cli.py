import typer
from rich.console import Console
from rich.panel import Panel

from config import APP_NAME, APP_VERSION, DEFAULT_REGION
from collectors.ec2 import EC2Collector
from collectors.ebs import EBSCollector
from exporter.excel import ExcelExporter

app = typer.Typer(
    help="AWS Cloud Inventory CLI",
    add_completion=False,
)

console = Console()


@app.command()
def version():
    """Show application version."""
    console.print(f"{APP_NAME} v{APP_VERSION}", style="bold green")


@app.command()
def export(
    region: str = typer.Option(
        DEFAULT_REGION,
        "--region",
        "-r",
        help="AWS region to collect inventory from.",
    ),
):
    """Export AWS inventory to an Excel workbook."""

    console.print(
        Panel.fit(
            f"[bold cyan]{APP_NAME}[/bold cyan]\nCollecting AWS inventory...",
            border_style="cyan",
        )
    )

    try:
        exporter = ExcelExporter()

        ec2_collector = EC2Collector(region)
        ec2_inventory = ec2_collector.collect()

        console.print(
            f"Found {len(ec2_inventory)} EC2 instance(s) in {region}."
        )

        exporter.write_sheet("EC2 Inventory", ec2_inventory)

        ebs_collector = EBSCollector(region)
        ebs_inventory = ebs_collector.collect()

        console.print(
            f"Found {len(ebs_inventory)} EBS volume(s) in {region}."
        )

        exporter.write_sheet("EBS Inventory", ebs_inventory)

        report = exporter.save()

        console.print(
            f"\nReport saved to: [bold green]{report}[/bold green]"
        )

    except Exception as err:
        console.print(f"[bold red]Error:[/bold red] {err}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
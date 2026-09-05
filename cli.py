import typer
from rich.console import Console
from rich.panel import Panel

from config import APP_NAME, APP_VERSION, DEFAULT_REGION
from collectors.ec2 import EC2Collector
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
    """Export EC2 inventory to an Excel workbook."""

    console.print(
        Panel.fit(
            f"[bold cyan]{APP_NAME}[/bold cyan]\nCollecting EC2 inventory...",
            border_style="cyan",
        )
    )

    try:
        collector = EC2Collector(region)
        inventory = collector.collect()

        console.print(f"Found {len(inventory)} EC2 instance(s) in {region}.")

        exporter = ExcelExporter()
        exporter.write_sheet("EC2 Inventory", inventory)

        report = exporter.save()

        console.print(f"\nReport saved to: [bold green]{report}[/bold green]")

    except Exception as err:
        console.print(f"[bold red]Error:[/bold red] {err}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
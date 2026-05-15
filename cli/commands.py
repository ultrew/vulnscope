import typer

from rich.console import Console
from rich.table import Table

from output.json_export import export_json
from core.scraper import fetch_programs
from core.classifier import classify_program


app = typer.Typer()
console = Console()


@app.command()
def scan(
    platform: str = None,
    difficulty: str = None,
    export: bool = False
):

    programs = fetch_programs()

    if platform:

        programs = [
            p for p in programs
            if p.get("platform", "").lower() == platform.lower()
        ]

    if difficulty:

        filtered = []

        for program in programs:

            level = classify_program(program)

            if level.lower() == difficulty.lower():
                filtered.append(program)

        programs = filtered

    console.print(f"[green]Programs fetched:[/green] {len(programs)}")

    if not programs:
        console.print("[red]No programs found.[/red]")
        return

    table = Table(title="VulnScope Results")

    table.add_column("Program", style="cyan")
    table.add_column("Platform", style="green")
    table.add_column("Difficulty", style="yellow")
    table.add_column("URL", style="magenta")

    for program in programs:

        table.add_row(
            program.get("name", "Unknown"),
            program.get("platform", "Unknown"),
            classify_program(program),
            program.get("url", "N/A")
        )

    console.print(table)

    if export:

        export_json(programs)

        console.print(
            "[green]Exported results to results.json[/green]"
        )

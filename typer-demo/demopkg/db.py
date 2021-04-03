import typer

from rich.console import Console

console = Console()
app = typer.Typer(name="db", help="Database commands.")


@app.command()
def create_db(table: str = typer.Option(..., prompt="What is the name of the table?", 
                                        confirmation_prompt=True)):
    """Pretend to make a database"""
    console.print(f"Creating table in database {table}", style="green")

@app.command()
def delete_db(table: str = typer.Option(..., prompt="What is the name of the table?", 
                                        confirmation_prompt=True)):
    """Pretend to delete a database"""
    sure = typer.confirm("Are you really really really sure?")
    if sure:
        console.print(f"Deleting table in database {table}", style="red")
    else:
        console.print(f"Back to safety!", style="green")

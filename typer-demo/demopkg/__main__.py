import typer
from typing import List
from pathlib import Path

from .db import app as db_app

app = typer.Typer(name="demo", add_completion=False, help="This is a demo app.")

# Here is where we attach subcommands as a group
app.add_typer(db_app, name="db")

@app.command()
def hello_world(name):
    """Say hello"""
    print(f"hello {name}!")

@app.command()
def goodbye_world(name):
    """Say goodbye"""
    print(f"goodbye {name}!")

@app.command()
def add(n1: int = typer.Argument(..., help="An integer"), 
        n2: int = typer.Argument(1, help="An integer")):
    """Add two numbers"""
    print(n1 + n2)

def check_file_exists(paths):
    for p in paths:
        if not p.exists():
            print(f"The path you've supplied {p} does not exist.")
            raise typer.Exit(code=1)
    return paths

@app.command()
def word_count(paths: List[Path] = typer.Argument(..., 
                                                  help="The file to count the words in.", 
                                                  callback=check_file_exists)):
    """Counts the number of words in a file"""
    for p in paths:
        texts = p.read_text().split("\n")
        n_words = len(set(w for t in texts for w in t.split(" ")))
        print(f"In total there are {n_words} words in {p}.")

# def talk(text, repeat=3, loud=False):
#     if loud:
#         text = text.upper()
#     for _ in range(repeat):
#         print(text) 

@app.command()
def talk(text: str = typer.Argument(..., help="The text to type."),
         repeat: int = typer.Option(1, help="Number of times to repeat."),
         loud: bool = typer.Option(False, is_flag=True)):
    """Talks some text below"""
    if loud:
        text = text.upper()
    for _ in range(repeat):
        print(text)


if __name__ == "__main__":
    app()

from atk_training_rama_proj1 import sayhello
import typer

app = typer.Typer()


@app.command()
def ex1(name: str):
    print("Hello from Hyderabad!!")
    sayhello.say_hello(name)


def main():
    app()

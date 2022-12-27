from atk_training_rama_proj1 import sayhello
import typer

app = typer.Typer()


@app.command()
def ex2(name: str):
    print("Hello buddy..I cracked you")
    print("Hello from Hyderabad!!")
    sayhello.say_hello(name)


def main():
    app()


if __name__ == "__main__":
    main()

import click

def print_error(msg: str):
    click.secho(msg, fg="red")

def print_success(msg: str):
    click.secho(msg, fg="green")

def print_warning(msg: str):
    click.secho(msg, fg="yellow")

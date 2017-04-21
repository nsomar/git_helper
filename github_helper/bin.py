import click
import sys
import os

from .lib import git_clean
from .lib import git_clean_remote

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()

@click.group(help="Provide helpers for git")
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def cli():
    pass

@cli.command()
@click.option("--head", default="master")
@click.argument('path', envvar='PWD', type=click.Path(exists=True))
def clean(head, path):
    """Remove uneeded branches"""
    git_clean.execute(path, head)


@cli.command("clean-remote")
@click.argument('path', envvar='PWD', type=click.Path(exists=True))
def clean_remote(path):
    """Remove uneeded branches"""
    git_clean_remote.execute(path)

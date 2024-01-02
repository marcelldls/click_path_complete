from pathlib import Path

import click

@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
def echo_path(name: Path):
    click.echo(f"Path: {name}")

@click.command()
@click.argument('name')
def echo_str(name: str):
    click.echo(f"String: {name}")


cli.add_command(echo_path)
cli.add_command(echo_str)

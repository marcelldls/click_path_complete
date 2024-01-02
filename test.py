import click

@click.group()
def cli():
    pass

@click.command()
@click.argument('name', type=click.Path())
def echo_path(name):
    click.echo(f"Path: {name}")

@click.command()
@click.argument('name')
def echo_str(name):
    click.echo(f"String: {name}")


cli.add_command(echo_path)
cli.add_command(echo_str)

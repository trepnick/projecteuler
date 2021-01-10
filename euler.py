import click
import commands


@click.group()
def cli():
    pass


for item in commands.all_commands:
    cli.add_command(item)


if __name__ == "__main__":
    cli()

from rich import print
import click
from logging import getLogger
from euler import solutions, scrapers


log = getLogger("rich")


@click.command()
@click.option("-n", default=1, help="number of the problem to solve")
def cli(n):
    log.debug("Getting problem description from euler.net website")
    print(scrapers.get_description(n))
    log.debug("Solving problem")
    try:
        print(solutions.all_solutions[n]())
    except IndexError:
        print(solutions.all_solutions[0]())
    log.debug("All operations complete")

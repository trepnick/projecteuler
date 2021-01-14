from rich import print
from rich.logging import RichHandler
import click
import logging
from euler import solutions, scrapers


log = logging.getLogger("rich")


@click.command()
@click.option("-n", default=1, help="number of the problem to solve")
@click.option("-v", is_flag=True, help="Verbose command output")
def _cli(n: int, v: bool):

    LOGLEVEL = logging.DEBUG if v else logging.ERROR
    FORMAT = "%(message)s"
    logging.basicConfig(
        level=LOGLEVEL,
        format=FORMAT,
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )

    log.info("Getting problem description from euler.net website")
    print(scrapers.get_description(n))
    log.info("Solving problem")
    try:
        print(solutions.all_solutions[n]())
    except IndexError:
        print(solutions.all_solutions[0]())
    log.info("All operations complete")

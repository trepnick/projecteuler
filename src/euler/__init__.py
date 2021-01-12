from euler.commands import cli
from rich.logging import RichHandler
import logging


LOGLEVEL = logging.ERROR
FORMAT = "%(message)s"
logging.basicConfig(
    level=LOGLEVEL,
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

#!/usr/bin/env python
"""Command-line interface."""
import click
from rich import traceback


@click.command()
@click.version_option(version="0.1.0", message=click.style("blablapackage Version: 0.1.0"))
def main() -> None:
    """blablapackage."""


if __name__ == "__main__":
    traceback.install()
    main(prog_name="blablapackage")  # pragma: no cover

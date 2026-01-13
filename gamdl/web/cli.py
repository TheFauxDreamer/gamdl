"""CLI entry point for gamdl web UI."""

import click

from gamdl.web.server import main as server_main


@click.command()
@click.option(
    "--host",
    default="127.0.0.1",
    help="Host to bind the server to",
    show_default=True,
)
@click.option(
    "--port",
    default=8080,
    help="Port to bind the server to",
    show_default=True,
    type=int,
)
def main(host: str, port: int):
    """Start the gamdl web UI server."""
    server_main(host=host, port=port)


if __name__ == "__main__":
    main()

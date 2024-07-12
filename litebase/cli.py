import click

# Register routes and sockets
from litebase import app


@click.group()
@click.option('--debug/--no-debug', default=False, is_flag=True, help='Enable or disable debug mode.')
@click.pass_context
def main(ctx, debug):
    """
    Welcome to Litebase CLI!
    """

    ctx.ensure_object(dict)
    ctx.obj['debug'] = debug

@main.command()
@click.pass_context
def serve(ctx):
    """
    Start the Litebase server
    """

    click.echo('Starting Litebase server...')

    # Starts the server
    app.run(debug=ctx.obj['debug'])

import typer
from glassbox.tui.app import GlassboxApp

app = typer.Typer(
    help="DevTools for LLM Applications",
    invoke_without_command=True,
)


@app.callback()
def main(ctx: typer.Context):
    """Launch Glassbox."""
    if ctx.invoked_subcommand is None:
        GlassboxApp().run()


@app.command()
def watch():
    """Launch Glassbox."""
    GlassboxApp().run()


if __name__ == "__main__":
    app()
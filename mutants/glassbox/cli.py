import typer

from glassbox.tui.app import GlassboxApp

app = typer.Typer(
    help="DevTools for LLM Applications",
    invoke_without_command=True,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@app.callback()
def main(ctx: typer.Context) -> None:
    """Launch Glassbox."""
    if ctx.invoked_subcommand is None:
        GlassboxApp().run()


@app.command()
def watch() -> None:
    """Launch Glassbox."""
    GlassboxApp().run()


@app.command()
def demo() -> None:
    """Run the deterministic scripted demo trace flow."""
    GlassboxApp(demo_mode=True).run()


if __name__ == "__main__":
    app()

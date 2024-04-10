"""The package information lookup screen."""

##############################################################################
# Textual imports.
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Input, Button
from textual.containers import Horizontal
from textual.binding import Binding

##############################################################################
# Local imports.
from ..widgets import PackageInfo


##############################################################################
class Lookup(Screen):
    """The package lookup screen."""

    CSS = """
    Header {
        HeaderIcon {
            visibility: hidden;
        }

        &.-tall {
            height: 1;
        }
    }

    Lookup {
        &> Horizontal {
            height: 5;
            border: blank;
            Input {
                width: 1fr;
            }
        }
    }
    """
    """The CSS for the screen."""

    BINDINGS = [Binding("f2", "app.switch_screen( 'stats' )", "Package Stats")]
    """list[ Binding ]: The bindings for the stats screen."""

    def compose(self) -> ComposeResult:
        """Compose the stats screen.

        Returns:
            ComposeResult: The stats screen's layout.
        """
        yield Header()
        with Horizontal():
            yield Input(placeholder="Name of the package to look up in PyPi")
            yield Button("Lookup")
        yield PackageInfo()
        yield Footer()

    def on_mount(self) -> None:
        """Configure the screen once loaded up."""
        self.query_one(Input).focus()

    async def on_input_submitted(self, _: Input.Submitted) -> None:
        """React to the user hitting enter in the input field."""
        await self.query_one(PackageInfo).show(self.query_one(Input).value)

    async def action_lookup(self, package: str) -> None:
        """React to a hyperlink of a project being clicked on.

        Args:
            package (str): The name of the package to look up.
        """
        self.query_one(Input).value = package
        self.query_one(Input).cursor_position = len(package)
        await self.query_one(PackageInfo).show(package)

    async def on_button_pressed(self, _: Button.Pressed) -> None:
        """React to the user pressing the lookup button."""
        await self.query_one(PackageInfo).show(self.query_one(Input).value)


### lookup.py ends here

import sys
import importlib

name = "cros-fetch"
version = "0.0"
branch = "main"
testmissingdep = False

required_dependencies = [
    ("textual", "textual"),
    ("rich", "rich"),
]

# injects dependency that doesnt exist
if testmissingdep:
    required_dependencies.append(("hyperspeed_booster", "hyper-speed-booster"))

# cool dependency checker that took me too long
def check_dependencies() -> bool:
    """checks for missing dependencies"""

    missing_packages = []

    for import_name, install_name in required_dependencies:
        try:
            importlib.import_module(import_name)
        except ImportError:
            missing_packages.append(install_name)

    if missing_packages:
        print("Missing required dependencies :[")
        print("The following packages need to be installed before running:")
        for pkg in missing_packages:
            print(f"  {pkg}")
        print("\nYou can install them using:")
        print(f"  pip install {' '.join(missing_packages)}")
        print("\nOr if your on macOS/linux:")
        print(f"  pip3 install {' '.join(missing_packages)}")
        return False

    return True

if not check_dependencies():
    sys.exit(1)

# textual
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class crosfetch(App):
    """larp larp larp sahur"""
    
    CSS = """
    Screen {
        align: center middle;
    }
    #message {
        width: 60;
        height: auto;
        border: solid green;
        background: $surface;
        content-align: center middle;
        padding: 1 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(
            "welcome to cros-fetch blud 😂🫱🫱", 
            id="message"
        )
        yield Footer()

if __name__ == "__main__":
    app = crosfetch()
    app.run()
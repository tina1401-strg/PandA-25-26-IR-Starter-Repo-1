# Acceptance test: transcript as executable spec
import io, sys, importlib
from pathlib import Path

# Import the app as a module
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from part1 import app  # type: ignore
from part1.constants import BANNER, HELP

def run_with_inputs(inputs):
    it = iter(inputs)
    out = io.StringIO()
    def fake_input(prompt=""):
        print(prompt, end="", file=out)
        try:
            return next(it)
        except StopIteration:
            raise EOFError
    # Capture prints by temporarily swapping stdout
    old_stdout = sys.stdout
    sys.stdout = out
    try:
        old_input = __builtins__["input"]
        __builtins__["input"] = fake_input  # type: ignore
        try:
            app.main()
        finally:
            __builtins__["input"] = old_input  # type: ignore
    finally:
        sys.stdout = old_stdout
    return out.getvalue()

def normalize(s: str) -> str:
    # Normalize newlines and strip trailing spaces on each line
    return "\n".join(line.rstrip() for line in s.replace("\r\n", "\n").replace("\r", "\n").split("\n"))

def test_interaction_snapshot():
    inputs = [
        ":help",
        "love",
        "and",
        "test",
        ":quit",
    ]
    got = normalize(run_with_inputs(inputs))
    expected = normalize(Path(__file__).with_name("snapshot_interaction.txt").read_text(encoding="utf-8"))
    assert got == expected, "Transcript does not match expected snapshot.\n\nGOT:\n" + got

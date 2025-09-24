# Run without pytest: python -m part1.tests.check_transcript
import io, sys
import builtins
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from part1 import app  # type: ignore

def run_with_inputs(inputs):
    it = iter(inputs)
    out = io.StringIO()
    def fake_input(prompt=""):
        print(prompt, end="", file=out)
        try:
            return next(it)
        except StopIteration:
            raise EOFError
    old_stdout = sys.stdout
    sys.stdout = out
    try:
        old_input = builtins.input
        builtins.input = fake_input  # type: ignore
        try:
            app.main()
        finally:
            builtins.input = old_input  # type: ignore
    finally:
        sys.stdout = old_stdout
    return out.getvalue()

def normalize(s: str) -> str:
    return "\n".join(line.rstrip() for line in s.replace("\r\n", "\n").replace("\r", "\n").split("\n"))

def main():
    inputs = [":help", "love", "and", "test", ":quit"]
    got = normalize(run_with_inputs(inputs))
    expected = normalize(Path(__file__).with_name("snapshot_interaction.txt").read_text(encoding="utf-8"))
    if got == expected:
        print("OK: Transcript matches snapshot.")
    else:
        print("FAIL: Transcript does not match snapshot.\n\nGOT:\n")
        print(got)

if __name__ == "__main__":
    main()

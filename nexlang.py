import sys
import time
import random
from pathlib import Path


# ---------------------------------------------------------
# NexLang: A custom Python flavour built on CPython
# ---------------------------------------------------------

# NEW FUNCTION 1
def show(*values, sep=" ", end="\n"):
    """Display output."""
    print(*values, sep=sep, end=end)


# NEW FUNCTION 2
def ask(prompt=""):
    """Accept input from the user."""
    return input(prompt)


# NEW FUNCTION 3
def pause(seconds):
    """Pause program execution."""
    time.sleep(float(seconds))


# NEW FUNCTION 4
def roll(minimum=1, maximum=100):
    """Generate a random integer."""
    minimum = int(minimum)
    maximum = int(maximum)

    if minimum > maximum:
        raise ValueError("Minimum cannot be greater than maximum.")

    return random.randint(minimum, maximum)


# NEW FUNCTION 5
def inside(value, low, high):
    """Check whether a value is within an inclusive range."""
    return low <= value <= high


# ---------------------------------------------------------
# NexLang Translator
# ---------------------------------------------------------

def translate(source):
    output = [
        "# Translated by NexLang",
        "import time",
        "import random",
    ]

    lines = source.splitlines()
    block_stack = []
    last_when_at_indent = {}

    for line_number, original_line in enumerate(lines, 1):

        stripped = original_line.strip()

        if not stripped or stripped.startswith("#"):
            output.append("")
            continue

        # Detect tabs in indentation
        leading = original_line[:len(original_line) - len(original_line.lstrip())]

        if "\t" in leading:
            raise SyntaxError(
                f"Line {line_number}: Use spaces instead of tabs."
            )

        indent = len(original_line) - len(original_line.lstrip(" "))

        if indent % 4 != 0:
            raise SyntaxError(
                f"Line {line_number}: Use 4 spaces for indentation."
            )

        # Close blocks when indentation decreases
        while block_stack and indent <= block_stack[-1]:
            block_stack.pop()

        expected_indent = 0 if not block_stack else block_stack[-1] + 4

        if indent != expected_indent:
            raise SyntaxError(
                f"Line {line_number}: Invalid indentation. "
                f"Expected {expected_indent} spaces."
            )

        prefix = " " * indent
        translated = stripped
        opens_block = False

        # KEYWORD 1: repeat
        if stripped.startswith("repeat ") and stripped.endswith(":"):

            count = stripped[len("repeat "):-1].strip()

            if not count:
                raise SyntaxError(
                    f"Line {line_number}: Missing repeat count."
                )

            translated = f"for _nexlang_i in range({count}):"
            opens_block = True
            last_when_at_indent[indent] = False

        # KEYWORD 2: when
        elif stripped.startswith("when ") and stripped.endswith(":"):

            condition = stripped[len("when "):-1].strip()

            if not condition:
                raise SyntaxError(
                    f"Line {line_number}: Missing condition."
                )

            translated = f"if {condition}:"
            opens_block = True
            last_when_at_indent[indent] = True

        # KEYWORD 3: otherwise
        elif stripped == "otherwise:":

            if not last_when_at_indent.get(indent, False):
                raise SyntaxError(
                    f"Line {line_number}: 'otherwise:' must follow "
                    f"a 'when' block."
                )

            translated = "else:"
            opens_block = True
            last_when_at_indent[indent] = False

        # KEYWORD 4: unless
        elif stripped.startswith("unless ") and stripped.endswith(":"):

            condition = stripped[len("unless "):-1].strip()

            if not condition:
                raise SyntaxError(
                    f"Line {line_number}: Missing condition."
                )

            translated = f"if not ({condition}):"
            opens_block = True
            last_when_at_indent[indent] = False

        # KEYWORD 5: forever
        elif stripped == "forever:":

            translated = "while True:"
            opens_block = True
            last_when_at_indent[indent] = False

        else:
            # Standard Python expressions, assignments and statements
            # are allowed inside NexLang programs.
            translated = stripped

            if indent in last_when_at_indent:
                last_when_at_indent[indent] = False

        output.append(prefix + translated)

        if opens_block:
            block_stack.append(indent)

    python_source = "\n".join(output)

    # Validate generated Python syntax using CPython
    compile(python_source, "<NexLang>", "exec")

    return python_source


# ---------------------------------------------------------
# NexLang File Runner
# ---------------------------------------------------------

def run_file(filename):

    path = Path(filename)

    if not path.is_file():
        print(f"File not found: {filename}")
        return 1

    try:
        source = path.read_text(encoding="utf-8")

        python_code = translate(source)

        environment = {
            "__name__": "__main__",
            "show": show,
            "ask": ask,
            "pause": pause,
            "roll": roll,
            "inside": inside,
        }

        compiled_code = compile(
            python_code,
            str(path),
            "exec"
        )

        exec(compiled_code, environment)

        return 0

    except Exception as error:
        print(f"NexLang Error: {error}")
        return 1


# ---------------------------------------------------------
# Command Line Interface
# ---------------------------------------------------------

def main():

    if len(sys.argv) != 2:
        print("NexLang 2.0")
        print("Usage: python nexlang.py <file.nx>")
        return 1

    return run_file(sys.argv[1])


if __name__ == "__main__":
    sys.exit(main())
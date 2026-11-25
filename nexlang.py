
import sys
import time
import re


def translate(source):
    output = ["import time"]

    lines = source.splitlines()
    indent_stack = [0]

    for line_number, line in enumerate(lines, 1):
        if not line.strip() or line.strip().startswith("#"):
            continue

        indent = len(line) - len(line.lstrip())
        stripped = line.strip()

        if indent % 4 != 0:
            raise SyntaxError(f"Line {line_number}: Use 4 spaces for indentation.")

        while indent < indent_stack[-1]:
            indent_stack.pop()

        if indent > indent_stack[-1]:
            if indent_stack[-1] == 0 or indent_stack[-1] + 4 != indent:
                raise SyntaxError(f"Line {line_number}: Invalid indentation.")

            indent_stack.append(indent)

        prefix = " " * indent

        if stripped.startswith("say "):
            message = stripped[4:].strip()

            if not message:
                raise SyntaxError(f"Line {line_number}: Missing message.")

            output.append(f"{prefix}print({message})")

        elif stripped.startswith("pause "):
            duration = stripped[6:].strip()

            if not duration:
                raise SyntaxError(f"Line {line_number}: Missing duration.")

            output.append(f"{prefix}time.sleep({duration})")

        elif stripped.startswith("loop ") and stripped.endswith(":"):
            count = stripped[5:-1].strip()

            if not count:
                raise SyntaxError(f"Line {line_number}: Missing loop count.")

            output.append(f"{prefix}for _ in range({count}):")

            indent_stack.append(indent + 4)

        else:
            raise SyntaxError(
                f"Line {line_number}: Unknown or invalid command '{stripped}'."
            )

    return "\n".join(output)


def run_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            source = file.read()

        python_code = translate(source)

        exec(compile(python_code, filename, "exec"), {})

    except FileNotFoundError:
        print(f"File not found: {filename}")

    except Exception as error:
        print(f"NexLang Error: {error}")


def main():
    if len(sys.argv) != 2:
        print("NexLang 1.1")
        print("Usage: python nexlang.py <file.nx>")
        return

    run_file(sys.argv[1])


if __name__ == "__main__":
    main()

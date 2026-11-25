# NexLang – A Custom Flavour of Python

NexLang is a lightweight experimental programming language built on top of CPython. It introduces five custom keywords and five additional built-in functions to provide a simple and readable Python-like coding experience.

NexLang programs use the `.nx` file extension. Its translator converts custom syntax into valid Python code, which is compiled and executed using the existing CPython compiler and Python Virtual Machine (PVM).

## Features

### Custom Keywords

| Keyword | Description |
|---|---|
| `repeat` | Repeats a block a specified number of times |
| `when` | Executes a block when a condition is true |
| `otherwise` | Provides an alternative conditional block |
| `unless` | Executes a block when a condition is false |
| `forever` | Creates an infinite loop |

### Built-in Functions

| Function | Description |
|---|---|
| `show()` | Displays output |
| `ask()` | Accepts user input |
| `pause()` | Pauses program execution |
| `roll()` | Generates a random integer |
| `inside()` | Checks whether a value is within a range |

## Architecture

NexLang Source (`.nx`) → NexLang Translator → Python Source Code → CPython Compiler → Bytecode → CPython PVM → Output

## Project Structure

```text
NexLang/
├── nexlang.py
├── README.md
├── LICENSE
├── examples/
│   └── hello.nx
└── tests/
    └── test_basic.py
```

## Requirements

- Python 3.10 or later
- Windows (for the provided executable)

## Run NexLang

Run a program using Python:

```bash
python nexlang.py examples/hello.nx
```

Or use the standalone Windows executable:

```bash
NexLang.exe examples/hello.nx
```

## Build the Executable

Install PyInstaller:

```bash
python -m pip install pyinstaller
```

Build:

```bash
python -m PyInstaller --onefile --console --name NexLang nexlang.py
```

The executable will be generated inside the `dist` folder.

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Jahidul Islam Shuba**
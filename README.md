# NexLang 2.1 🐍
### A Custom Python Flavour Built on CPython

NexLang is an experimental Python-like programming language built on top of **CPython**. It introduces five custom keywords and five additional built-in functions to make programming more expressive and beginner-friendly.

NexLang uses the `.nx` file extension. Its translator converts NexLang source code into valid Python code, which is then compiled and executed using the existing CPython compiler and Python Virtual Machine (PVM).

> **Project Goal:** Create a custom flavour of Python with its own syntax, functions, translator, and standalone Windows executable.

---

## ✨ Features

### 1. Five Custom Keywords

| Keyword | Description |
|---|---|
| `repeat` | Repeats a block a specified number of times |
| `when` | Executes a block when a condition is true |
| `otherwise` | Provides an alternative conditional block |
| `unless` | Executes a block when a condition is false |
| `forever` | Creates an infinite loop |

### 2. Five Built-in Functions

| Function | Description |
|---|---|
| `show()` | Displays output |
| `ask()` | Accepts user input |
| `pause()` | Pauses program execution |
| `roll()` | Generates a random integer |
| `inside()` | Checks whether a value is within a specified range |

---

## ⚙️ How NexLang Works

NexLang does not implement a completely new virtual machine. Instead, it builds on the existing CPython execution environment.

**Execution pipeline:**

```text
NexLang Source Code (.nx)
          |
          v
    NexLang Translator
          |
          v
   Generated Python Code
          |
          v
     CPython Compiler
          |
          v
      Python Bytecode
          |
          v
       CPython PVM
          |
          v
         Output
```

This approach allows NexLang to introduce custom syntax while reusing the reliability and execution capabilities of CPython.

---

## 🚀 Getting Started

### Requirements

- Windows 10 or later (for the provided executable)
- Python 3.10 or later (for running through the translator and building)
- PyInstaller (only required to build the executable)

### Option 1: Run Using Python

Clone the repository:

```bash
git clone https://github.com/jahidul-uiux/NexLang.git
```

Open the project directory:

```bash
cd NexLang
```

Run a NexLang program:

```bash
python nexlang.py examples/hello.nx
```

### Option 2: Run Using the Windows Executable

A standalone executable is included in the `dist` directory.

From the project root, run:

```powershell
.\dist\NexLang.exe examples\hello.nx
```

You do not need to install Python separately to run the packaged executable.

---

## 💻 NexLang Example

Create a file named `hello.nx`:

```python
# Get user input
name = ask("Enter your name: ")

# Display output
show("Hello,", name)
show("Welcome to NexLang!")

# Repeat a block three times
repeat 3:
    show("I am learning NexLang!")

# Generate a random number
age = roll(18, 25)

show("Your generated age is:", age)

# Conditional execution
when age >= 18:
    show("You are an adult.")
otherwise:
    show("You are under 18.")

# Execute when condition is false
unless name == "":
    show("Thanks for using NexLang!")

# Check a range
when inside(age, 18, 30):
    show("Your age is within the range.")
```

Run it:

```powershell
.\dist\NexLang.exe hello.nx
```

---

## 🛠️ Build the Executable

You can generate your own Windows executable using PyInstaller.

Install PyInstaller:

```bash
python -m pip install pyinstaller
```

Build NexLang:

```bash
python -m PyInstaller --onefile --console --clean --name NexLang nexlang.py
```

After the build completes, the executable will be available at:

```text
dist/NexLang.exe
```

---

## 🧪 Run Tests

NexLang includes a unit test suite covering its custom keywords and built-in functions.

Run all tests:

```bash
python -m unittest discover -s tests -v
```

The current test suite contains 11 tests, including a nested-block translation test.

---

## 📁 Project Structure

```text
NexLang/
│
├── nexlang.py             # NexLang translator and execution engine
├── NexLang.spec           # PyInstaller build configuration
├── README.md              # Project documentation
├── LICENSE                # MIT License
├── .gitignore             # Ignored generated files
│
├── examples/
│   └── hello.nx           # Sample NexLang program
│
├── tests/
│   └── test_basic.py      # Unit tests
│
└── dist/
    └── NexLang.exe        # Standalone Windows executable
```

---

## 🔮 Future Improvements

- Better syntax error messages
- Improved nested-block handling
- More built-in functions
- Additional example programs
- Improved command-line interface
- Support for more operating systems

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Jahidul Islam Shuba**

B.Tech Computer Science and Engineering Student

GitHub: [@jahidul-uiux](https://github.com/jahidul-uiux)

**Project Repository:** [NexLang on GitHub](https://github.com/jahidul-uiux/NexLang)

---

*Built as an academic project to explore programming language design, source-code translation, and the CPython execution process.*
# NexLang

**NexLang** is a lightweight experimental programming language built with Python.

It introduces simple, beginner-friendly commands that are translated into executable Python code.

## Features

- `say` — Display messages
- `loop` — Repeat instructions
- `pause` — Add execution delays
- Simple Python-based translator
- Lightweight and beginner-friendly

## Example

```python
say "Hello, World!"

loop 3:
    say "Welcome to NexLang!"

pause 1
```

## Run NexLang

```bash
python nexlang.py examples/hello.nx
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Technology

- Python 3
- Python Standard Library

## Project Status

Version 1.0 — Experimental prototype.

## License

MIT License (planned).

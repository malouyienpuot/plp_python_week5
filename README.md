# Password Generator Module

A small Python package that generates secure random passwords with configurable character sets and validation.

## Features
- Generate passwords of any length
- Include or exclude uppercase, lowercase, digits, and symbols
- Remove ambiguous characters when needed
- Use either the Python API or the command-line interface

## Installation

From the project root:

```bash
python -m pip install -e .
```

## Usage

### Python API

```python
from password_generator import generate_password

password = generate_password(length=16)
print(password)
```

### Command line

```bash
python -m password_generator --length 16 --avoid-ambiguous
```

## Running tests

```bash
python -m pytest -q
```

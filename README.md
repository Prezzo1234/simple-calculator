<<<<<<< HEAD
 Simple Calculator - Jaseci Project

A simple calculator built using **Jaseci**, designed for beginners to explore Jaseci’s core features like **actions**, **walks**, and **nodes**. This project demonstrates how to create interactive logic using Jac programs combined with Python actions.

---

## Project Overview

The project allows users to perform basic arithmetic operations (addition, subtraction, multiplication, division) through a simple command-line interface. It’s a perfect starting point for learning Jaseci programming.

---

## Project Structure
# Simple Calculator - Jaseci Project

A simple calculator built using **Jaseci**, designed for beginners to explore Jaseci’s core features like **actions**, **walks**, and **nodes**. This project demonstrates how to create interactive logic using Jac programs combined with Python actions.

---

## Project Overview

The project allows users to perform basic arithmetic operations (addition, subtraction, multiplication, division) through a simple command-line interface. It’s a perfect starting point for learning Jaseci programming.

---

## Project Structure (remote example)

This repository previously contained a larger example layout. The key elements of that remote README are preserved below; local assignment files are described in their own section after this.

simple-calculator/ (example layout)
- actions/
- problems/
- main.jac
- README.md

## Prerequisites (remote example)

- Python 3.12
- Virtual environment (`venv`)
- Jaseci (example listed v1.4.2.6)

## Installation & Setup (remote example)

Follow the remote README instructions if you're using the larger example: create and activate a virtualenv, install Jaseci and any action dependencies.

---

# Local assignment files (this fork)

This fork contains a minimal, runnable Jac assignment suitable for submission. Files in this folder are:

- `calculator.jac` — Jac source file with basic arithmetic functions and example usage.
- `runner.py` — Python helper that calls the `jac` CLI to run the Jac program or evaluate a single operation.
- `requirements.txt` — Python dependencies (installs the Jac runtime/CLI via pip).
- `tests/test_calculator.py` — Simple pytest that exercises the runner (requires `jac` to be installed in the env).
- `.gitignore` — ignores virtualenv files and temp outputs.

## How to run (local)

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
```

2. Run the Jac example (prints a few sample calculations):

```bash
jac run calculator.jac
```

3. Or use the Python runner to evaluate a single operation (uses the `jac` CLI under the hood):

```bash
python runner.py add 2 3
python runner.py div 8 2
```

4. Run tests (requires `jac` available in the environment):

```bash
pytest -q
```

## Notes
- This project relies on the `jac` CLI provided by the `jaclang` package. If you can't install packages on your system, the `calculator.jac` file is a standalone Jac program that can be submitted along with this README.

How to run

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
```

2. Run the Jac example (prints a few sample calculations):

```bash
jac run calculator.jac
```

3. Or use the Python runner to evaluate a single operation (uses the `jac` CLI under the hood):

```bash
python runner.py add 2 3
python runner.py div 8 2
```

4. Run tests (requires `jac` available in the environment):

```bash
pytest -q
```

Notes
- This project relies on the `jac` CLI provided by the `jaclang` package. If you can't install packages on your system, the `calculator.jac` file is a standalone Jac program that can be submitted along with this README.
>>>>>>> 2f807af (Add Jaseci/Jac simple calculator project)

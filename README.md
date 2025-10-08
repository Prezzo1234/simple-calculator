 Simple Calculator - Jaseci Project

A simple calculator built using **Jaseci**, designed for beginners to explore Jaseci’s core features like **actions**, **walks**, and **nodes**. This project demonstrates how to create interactive logic using Jac programs combined with Python actions.

---

## Project Overview

The project allows users to perform basic arithmetic operations (addition, subtraction, multiplication, division) through a simple command-line interface. It’s a perfect starting point for learning Jaseci programming.

---

## Project Structure

simple-calculator/
├── actions/
│ └── init.py # Python actions used by Jac
├── problems/
│ └── calculator.jac # Jac program defining calculator logic
├── main.jac # Entry point Jac program
├── venv/ # Python virtual environment
└── README.md # Project documentation

yaml
Copy code

---

## Prerequisites

Before running the project, ensure you have:

- Python 3.12 installed
- Virtual environment (`venv`)
- Jaseci 1.4.2.6 installed
- Required Python packages for actions (e.g., FastAPI, if used)
- `distutils` installed for building packages

---

## Installation & Setup

1. **Clone the repository**:

```bash
git clone <your-repo-url>
cd simple-calculator
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Upgrade pip, setuptools, and wheel:

bash
Copy code
pip install --upgrade pip setuptools wheel
Install Jaseci and dependencies:

bash
Copy code
pip install jaseci==1.4.2.6
pip install fastapi
# Install any other packages your actions use
How to Run the Calculator
Run the main Jac program:

bash
Copy code
jac run main.jac
Follow the on-screen prompts to input numbers and operations. The calculator will return the result for your operation.

How It Works
This project uses Jaseci, a framework for building autonomous agents, which relies on three main concepts:

Actions (actions/__init__.py)
Python functions that define tasks your Jac program can perform. For example, adding two numbers or calculating a result.

Walks (main.jac)
Sequences of steps that guide your agents through tasks. In this project, the walk guides the calculator flow from input to output.

Jac Programs (calculator.jac)
Jac is a high-level language used to define the logic of your agents. Here, it handles arithmetic operations and user input/output.

Tips for Beginners
Keep Python actions simple at first, only implement the arithmetic operations.

Test each part individually: first actions, then Jac logic.

Make sure your virtual environment is activated before running Jac programs.

Use clear variable names to track numbers and operations in the Jac program.

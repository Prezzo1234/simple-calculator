#!/usr/bin/env python3
"""Simple runner that invokes the jac CLI to run the Jac program or a one-off operation."""
import sys
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).parent


def check_jac_available() -> str:
    jac_bin = shutil.which("jac")
    if not jac_bin:
        raise SystemExit("Error: 'jac' executable not found. Install jaclang (pip install jaclang) and ensure it's on PATH.")
    return jac_bin


def run_jac_file(jac_path: Path) -> int:
    jac = check_jac_available()
    proc = subprocess.run([jac, "run", str(jac_path)], check=False)
    return proc.returncode


def eval_operation(op: str, a: str, b: str) -> int:
    """Evaluate a single operation by creating a tiny Jac snippet and running it."""
    jac = check_jac_available()
    snippet = {
        "add": f"with entry {{ print({a} + {b}); }}",
        "sub": f"with entry {{ print({a} - {b}); }}",
        "mul": f"with entry {{ print({a} * {b}); }}",
        "div": f"with entry {{ if ({b} == 0) {{ print('error: division by zero'); }} else {{ print({a} / {b}); }} }}",
    }
    if op not in snippet:
        raise SystemExit(f"Unsupported op: {op}. choose one of add, sub, mul, div")

    # Write snippet to a temp file
    tmp = ROOT / ".tmp_op.jac"
    tmp.write_text(snippet[op])
    try:
        return run_jac_file(tmp)
    finally:
        try:
            tmp.unlink()
        except Exception:
            pass


def main(argv):
    if len(argv) == 1:
        # run the full Jac program
        return run_jac_file(ROOT / "calculator.jac")

    # evaluate one operation: runner.py <op> a b
    if len(argv) != 4:
        print("Usage:\n  python runner.py            # run calculator.jac\n  python runner.py add 2 3   # evaluate add")
        return 2

    op, a, b = argv[1], argv[2], argv[3]
    return eval_operation(op, a, b)


if __name__ == "__main__":
    sys.exit(main(sys.argv))

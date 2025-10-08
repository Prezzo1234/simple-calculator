import shutil
from pathlib import Path
import subprocess


ROOT = Path(__file__).parent.parent


def jac_available():
    return shutil.which("jac") is not None


def test_calculator_jac_run(tmp_path):
    if not jac_available():
        import pytest
        pytest.skip("jac CLI not installed")

    proc = subprocess.run(["jac", "run", str(ROOT / "calculator.jac")], capture_output=True, text=True)
    assert proc.returncode == 0
    out = proc.stdout
    # Basic assertions that show the program printed sample calculations
    assert "2 + 3 = 5" in out
    assert "10 - 4 = 6" in out
    assert "6 * 7 = 42" in out

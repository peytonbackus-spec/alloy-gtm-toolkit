#!/usr/bin/env python3
"""
Unit Test Execution Script for Alloy GTM Toolkit Modules
Runs every module script as a subprocess and verifies it exits cleanly.
"""
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).parent
MODULES_DIR = REPO_ROOT / "modules"

def discover_scripts():
    return sorted(MODULES_DIR.rglob("*.py"))

class TestAlloyGTMToolkit(unittest.TestCase):
    pass

def make_test(script_path):
    def test(self):
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True, text=True, timeout=30
        )
        self.assertEqual(
            result.returncode, 0,
            msg=f"{script_path} failed:\n{result.stderr}"
        )
    return test

for script in discover_scripts():
    test_name = f"test_{script.stem}"
    setattr(TestAlloyGTMToolkit, test_name, make_test(script))

if __name__ == "__main__":
    print("=== RUNNING ALLOY TOOLKIT SUITE VERIFICATION ===")
    scripts = discover_scripts()
    print(f"[+] Discovered {len(scripts)} module scripts under modules/\n")
    unittest.main(verbosity=2)

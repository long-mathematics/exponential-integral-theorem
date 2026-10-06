#!/usr/bin/env python3
"""Run the finite exact certificates accompanying Paper V.

Requires SymPy. No network access, manuscript writes, or repository writes.
These computations are regression checks, not formal verification of the theorem.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--suite', choices=('all', 'example', 'formal'), default='all')
    args = parser.parse_args()
    scripts = {
        'example': ROOT / 'notes/candidates/2026-10-06-single-chain/frozen/check_generic_example_audited.py',
        'formal': ROOT / 'scripts/check_single_chain_formal.py',
    }
    for name, path in scripts.items():
        if args.suite not in ('all', name):
            continue
        if not path.is_file():
            raise RuntimeError(f'Missing certificate: {path}')
        subprocess.run([sys.executable, str(path)], cwd=ROOT, check=True, timeout=120)


if __name__ == '__main__':
    main()

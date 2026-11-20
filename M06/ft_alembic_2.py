#!/opt/pyenv/shims/python

import alchemy.elements

if __name__ == "__main__":
    print(
        "=== Alembic 2 ===",
        "Accessing alchemy/elements.py using 'import ...'structure",
        sep='\n')
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")

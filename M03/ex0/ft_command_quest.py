#!/opt/pyenv/shims/python

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    p_name: str = sys.argv[0]
    print(f"Program name: {p_name}")
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(sys.argv)}\n")

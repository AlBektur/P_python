#!/opt/pyenv/shims/python

import sys

if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) == 2:
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(f"{sys.argv[1]}", 'r')
        except Exception as e:
            print(f"Error opening file {e}")
        else:
            print("---\n")
            print(file.read(), end="")
            print("---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
    else:
        print("Usage: ft_ancient_text.py <file>")

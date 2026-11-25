#!/opt/pyenv/shims/python


import sys
import os
import site

if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print("\nMATRIX STATUS: You're still plugged in")
        print("Virtual Environment: None detected\n")
        print(f"Current Python: {sys.executable}")
        print(
            "WARNING: You're in the global environment!"
            "The machines can see everything you install.\n"
        )
        print(
            "To enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n\n"
            "Then run this program again."
        )
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")

        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")

        print(
            "\nSUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting\n"
            "the global system.\n\n"
        )
        print("Package installation path:")
        print(site.getusersitepackages())

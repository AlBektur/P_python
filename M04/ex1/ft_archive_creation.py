#!/opt/pyenv/shims/python

import sys

if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) == 2:
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(f"{sys.argv[1]}", 'r')
            print("---\n")
            cont = file.read()
            print(cont)
            print("---")
            file.close()
            if file.closed:
                print(f"File '{sys.argv[1]}' closed.\n")

            print("Transform data:", '---\n', sep='\n')
            contento: list = cont.split('\n')
            del contento[-1]
            content: list = [i + '#' for i in contento]
            for i in content:
                print(i)
            print('\n---')
            new_file_name = input("Enter new file name (or empty): ")
            if new_file_name:
                new_file = open(new_file_name, 'w')
                try:
                    print(f"Saving data to '{new_file_name}'")
                    for i in content:
                        new_file.write(i + '\n')
                finally:
                    new_file.close()
                print(f"Data saved in file '{new_file_name}'.")
            else:
                print("Not saving data.")

        except Exception as e:
            print(f"Error opening file {e}")
    else:
        print("Usage: ft_archive_creation.py <file>")

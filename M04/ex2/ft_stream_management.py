#!/opt/pyenv/shims/python

import sys

if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")

    if len(sys.argv) == 2:
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1])
            file_content = file.read()
            print('---\n')
            print(file_content)
            print('---')
            file.close()
            print(f"File '{sys.argv[1]}'closed.\n")

            print("Transform data:", '---\n', sep='\n')
            content_list: list = file_content.split('\n')
            del content_list[-1]
            content = [x + '#' for x in content_list]
            for i in content:
                print(i)
            print('\n---')
            print("Enter new file name (or empty): ", end='')
            sys.stdout.flush()
            file_name = sys.stdin.readline()
            new_file_name = file_name[:-1]
            if new_file_name:
                try:
                    new_file = open(new_file_name, 'w')
                    print(f"Saving data to '{new_file_name}'")
                    for i in content:
                        new_file.write(i + '\n')
                    print(f"Data saved in file '{new_file_name}'.")
                except Exception as e:
                    print(
                        f"[STDERR] Error opening file"
                        f"'{new_file}': {e}", file=sys.stderr
                        )
            else:
                print("Data not saved.")
        except Exception as e:
            print(
                f"[STDERR] Error opening file"
                f"'{sys.argv[1]}': {e}", file=sys.stderr
                )
    else:
        print("Usage: ft_archive_creation.txt <file>")

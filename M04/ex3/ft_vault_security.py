#!/opt/pyenv/shims/python

def secure_archive(file_name: str, mode: str, content:str="") -> tuple:
    try:
        with open(file_name, mode) as file:
            if mode == "w":
                file.write(content)
                return (True, 'Content successfully written to file')
            else:
                content = file.read()
                return (True, content)
    except Exception as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive'to read from a nonexistent file:")
    res = secure_archive('/not/existing/file', 'r')
    print(res)

    print("\nUsing 'secure_archive'to read from an inaccessible file:")
    res = secure_archive('/etc/master.passwd', 'r')
    print(res)

    print("\nUsing 'secure_archive'to read from a regular file:")
    res = secure_archive('ancient_fragment.txt', 'r')
    print(res)

    print("\nUsing 'secure_archive'to write previous content to a new file:")
    res = secure_archive('towrite', 'w', 'Something')
    print(res)

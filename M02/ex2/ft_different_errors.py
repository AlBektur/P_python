#!/opt/pyenv/shims/python3

def garden_operations(operation_number):
    if operation_number == 0:
        number = 'abc'
        number = int(number)
    elif operation_number == 1:
        123 / 0
    elif operation_number == 2:
        open('file.txtt', 'r')
    elif operation_number == 3:
        "hello" + 123
    elif operation_number == 4:
        1 + 1


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    i = 0
    while i <= 4:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully\n")
        except ValueError as e:
            print(f"Caught ValueError: {e}\n")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}\n")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}\n")
        except TypeError as e:
            print(f"Caught TypeError: {e}\n")

        i += 1
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

#!/opt/pyenv/shims/python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    print("Input data is '25'")
    n = input_temperature("25")
    print(f"Temperature is now {n}°C")

    print("\nInput data is 'abc'")
    try:
        n = input_temperature("abc")
        print(f"Temperature is now {n}°C")
    except Exception as err:
        print(f"Caught input_temperature error: {err}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

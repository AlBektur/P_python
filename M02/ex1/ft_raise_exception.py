#!/opt/pyenv/shims/python3

def input_temperature(temp_str: str) -> int:
    res = int(temp_str)
    if res < 0:
        raise Exception(f"{res}°C is too cold for plants (min 0°C)")
    elif res > 40:
        raise Exception(f"{res}°C is too hot for plants (max 40°C)")
    return res


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    values = ['25', 'abc', '100', '-50']

    for i in values:
        print(f"Input data is '{i}'")
        try:
            res = input_temperature(i)
            print(f"Temperature is now {res}°C\n")
        except Exception as e:
            print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

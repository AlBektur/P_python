#!/opt/pyenv/shims/python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        if height >= 0:
            self._height = height
        else:
            self._height = 0
            print(
                f"Given invalid value ({height}), setted default value 0\n"
                f"Pass correct value by using set_height method"
                )
        if age >= 0:
            self._age = age
        else:
            self._age = 0
            print(
                f"Given invalid value ({age}), setted default value 0\n"
                f"Pass correct value by using set_age method"
                )

    def set_height(self, new_height) -> None:
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {new_height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age) -> None:
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {new_age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def info(self) -> None:
        temp_var: float = float(self._height)
        print(f"{self.name}: {temp_var}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    p1.info()
    print()
    p1.set_height(25)
    p1.set_age(30)
    print()
    p1.set_height(-25)
    p1.set_age(-30)
    print()
    print("Current state: ", end="")
    p1.info()

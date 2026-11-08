#!/opt/pyenv/shims/python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def set_height(self, new_height) -> None:
        if new_height > 0:
            self._height = new_height
            print(f"Height updated: {new_height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age) -> None:
        if new_age > 0:
            self._age = new_age
            print(f"Age updated: {new_age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

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

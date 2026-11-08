#!/opt/pyenv/shims/python3
class Plant():
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height = self.height + 0.8

    def days(self) -> None:
        self.age = self.age + 1

    def info(self) -> None:
        temp_var = round(self.height, 1)
        print(f"{self.name}: {temp_var}cm, {self.age} days old")

    def stats(self, init_height: float) -> None:
        temp_var = round(self.height - init_height, 1)
        print(f"Growth this week: {temp_var}cm")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    p1 = Plant("Rose", 25., 30)
    p1.info()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        p1.grow()
        p1.days()
        p1.info()
    p1.stats(25)

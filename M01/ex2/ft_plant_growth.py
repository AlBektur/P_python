#!/opt/pyenv/shims/python3
class Plant():
    def __init__(self, name: str, height: float, age_days: int):
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self) -> None:
        if self.name == "Rose":
            self.height = self.height + 0.8
        elif self.name == "Sunflower":
            self.height = self.height + 2
        elif self.name == "Cactus":
            self.height = self.height + 0.1
        else:
            self.height = self.height + 1

    def age(self) -> None:
        self.age_days = self.age_days + 1

    def info(self) -> None:
        temp_var = round(self.height, 1)
        print(f"{self.name}: {temp_var}cm, {self.age_days} days old")

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
        p1.age()
        p1.info()
    p1.stats(25)

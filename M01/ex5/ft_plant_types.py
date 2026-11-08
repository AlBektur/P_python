#!/opt/pyenv/shims/python3

class Plant():
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

        def show(self) -> None:
            pass

        def grow_age(self) -> None:
            pass


class Flower(Plant):
    def __init__(self, name, height, age, color, bloom_status=0) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloom_status = bloom_status

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.bloom_status = 1

    def show(self) -> None:
        temp_var: float = float(self.height)
        print(f"{self.name}: {temp_var}cm, {self.age} days old")
        print(f"Color: {self.color}")
        if self.bloom_status == 1:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, td: int) -> None:
        super().__init__(name, height, age)
        self.td = td

    def produce_shade(self) -> None:
        temp_var: float = float(self.height)
        temp_var_2: float = float(self.td)
        print("[asking the oak to produce shade]")
        print(
            f"Tree {self.name} now produces a shade"
            f" of {temp_var}cm long and {temp_var_2}cm wide."
            )

    def show(self) -> None:
        temp_var: float = float(self.height)
        temp_var_2: float = float(self.td)
        print(f"{self.name}: {temp_var}cm, {self.age} days old")
        print(f"Trunk diameter: {temp_var_2}")


class Vegetable(Plant):
    def __init__(self, name, height, age, hs, nv=0) -> None:
        super().__init__(name, height, age)
        self.hs = hs
        self.nv = nv

    def grow_age(self, days) -> None:
        print(f"[make tomato grow and age for {days} days]")
        self.age = self.age + days
        self.nv = self.nv + 20
        self.height = self.height + (days * 2.1)

    def show(self) -> None:
        temp_var: float = float(self.height)
        print(f"{self.name}: {temp_var}cm, {self.age} days old")
        print(f"Harvest season: {self.hs}")
        print(f"Nutritional value: {self.nv}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    flower.bloom()
    flower.show()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    tree.produce_shade()
    print()

    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5, 10, "April")
    vegetable.show()
    vegetable.grow_age(20)
    vegetable.show()

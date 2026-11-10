#!/opt/pyenv/shims/python3

class Plant():
    class Stats:
        data = {

            "flower": {"grow": 0, "age": 0, "show": 0},
            "tree": {"grow": 0, "age": 0, "show": 0},
            "seed": {"grow": 0, "age": 0, "show": 0},
            "Unknown plant": {"grow": 0, "age": 0, "show": 0}
        }

        @classmethod
        def display_stats(cls, name: str, obj) -> None:
            print(f"[statistics for {name}]")
            print(
                f"Stats: {cls.data[name]['grow']} grow, "
                f"{cls.data[name]['age']} age, "
                f"{cls.data[name]['show']} show"
            )
            if isinstance(obj, Tree):
                print(f"{obj.shade} shade")

    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    @staticmethod
    def check_year(days: int) -> bool:
        if days > 365:
            return True
        else:
            return False

    def show(self) -> None:
        print(
            f"{self.name}: {float(self.height)}cm, "
            f"{self.age} days old"
        )
        self.Stats.data["Unknown plant"]["show"] += 1

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloom_status = 0

    def grow_bloom(self, days: int, bloom: bool) -> None:
        print("[asking the rose to grow and bloom]")
        self.height = self.height + (days * 0.8)
        if bloom:
            self.bloom_status = 1
        self.Stats.data["flower"]["grow"] += 1

    def show(self):
        temp_float: float = float(self.height)
        print(f"{self.name}: {temp_float}cm, {self.age} days old")
        print(f"Color: {self.color}")
        if self.bloom_status == 0:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

        self.Stats.data["flower"]["show"] += 1


class Tree(Plant):
    def __init__(self, name, height, age, td) -> None:
        super().__init__(name, height, age)
        self.td = td
        self.shade = 0

    def produce_shade(self) -> None:
        temp_height: float = float(self.height)
        temp_width: float = float(self.td)
        print("[asking the oak to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of",
            f"{temp_height}cm long and {temp_width}cm wide"
            )
        self.shade += 1

    def show(self):
        temp_float: float = float(self.height)
        temp_float_2: float = float(self.td)
        print(f"{self.name}: {temp_float}cm, {self.age} days old")
        print(f"Trunk diameter: {temp_float_2}cm")
        self.Stats.data["tree"]["show"] += 1


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seed = 0

    def grow_age_bloom(self, days: int, bloom: bool) -> None:
        print("[make sunflower grow, age and bloom]")
        self.height += days * 1.5
        self.age += days
        if bloom:
            self.bloom_status += 1
        if self.bloom_status == 1:
            self.seed = 42
        self.Stats.data["seed"]["age"] += 1
        self.Stats.data["seed"]["grow"] += 1

    def show(self):
        temp_float: float = float(self.height)
        print(f"{self.name}: {temp_float}cm, {self.age} days old")
        print(f"Color: {self.color}")
        if self.bloom_status == 0:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")
        print(f"Seeds: {self.seed}")
        self.Stats.data["seed"]["show"] += 1


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_year(400)}\n")

    print("=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    flower.Stats.display_stats("flower", flower)
    flower.grow_bloom(10, True)
    flower.show()
    flower.Stats.display_stats("flower", flower)

    print("\n=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    tree.Stats.display_stats("tree", tree)
    tree.produce_shade()
    tree.Stats.display_stats("tree", tree)

    print("\n=== Seed")
    seed = Seed("Sunflower", 80, 45, 'yellow')
    seed.show()
    seed.grow_age_bloom(20, True)
    seed.show()
    seed.Stats.display_stats("seed", seed)

    print("\n=== Anonymous")
    an = Plant.create_anonymous()
    an.show()
    an.Stats.display_stats("Unknown plant", seed)

#!/opt/pyenv/shims/python3

class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height = self.height + 0.8

    def show(self) -> None:
        temp_var = float(self.height)
        print(f"{self.name}: {temp_var}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plants_as_obj = []
    plant_in_dict = {
        "Rose": {"height": 25, "age": 30},
        "Oak": {"height": 200, "age": 365},
        "Cactus": {"height": 5, "age": 90},
        "Sunflower": {"height": 80, "age": 45},
        "Fern": {"height": 15, "age": 120}
    }

    for keys, values in plant_in_dict.items():
        plants_as_obj.append(Plant(keys, values["height"], values["age"]))
    for i in plants_as_obj:
        print("Created: ", end="")
        i.show()

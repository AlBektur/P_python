#!/opt/pyenv/shims/python3

class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return self.message


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


class Garden():
    def __init__(self, tank: int, plant_status: str) -> None:
        self.tank = tank
        self.plant_status = plant_status


class Plant(Garden):
    def __init__(self, name: str, tank: int, plant_status: str) -> None:
        super().__init__(tank, plant_status)
        self.name = name


def main() -> None:
    print("=== Custom Garden Errors Demo ==\n")
    try:
        print("Testing PlantError...")
        p1 = Plant("tomato", 10, 'wilting')
        if p1.plant_status == 'wilting':
            raise PlantError(f"The {p1.name} plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    try:
        print("Testing WaterError...")
        p2 = Plant("tomato", 0, 'ok')
        if p2.tank < 1:
            raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    try:
        p3 = Plant("tomato", 0, 'wilting')
        if p3.tank < 1:
            raise GardenError(f"The {p3.name} plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        print("\nTesting catching all garden errors...")
        if p3.plant_status == 'wilting':
            raise GardenError("Not enough water in the tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()

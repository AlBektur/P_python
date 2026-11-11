#!/opt/pyenv/shims/python3

class PlantError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class Plant():
    def __init__(self, name: str) -> None:
        self.name = name


def water_plant(plant_name: str) -> None:
    temp_name = plant_name.capitalize()
    if temp_name == plant_name:
        print(f'Watering {plant_name}: [OK]')
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system():
    print("=== Garden Watering System ===\n")

    p_list = ['Tomato', 'Letucce', 'Carrots']
    p_list_err = ['Tomato', 'letucce', 'Carrots']

    print("Testing valid plants...")
    try:
        print("Opening watering system")
        for i in p_list:
            water_plant(i)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    try:
        print("Opening watering system")
        for i in p_list_err:
            water_plant(i)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    test_watering_system()
    print("\nCleanup always happens, even with errors!")

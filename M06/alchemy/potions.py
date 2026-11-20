#!/opt/pyenv/shims/python


from elements import create_fire, create_water
from alchemy.elements import create_earth, create_air


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{create_earth()}' and '{create_air()}'")


def strength_potion() -> str:
    return (
        f"Strength potion brewed with ’{create_fire()}’"
        f" and ’{create_water()}’")


if __name__ == "__main__":
    print(f"Heling potion: {healing_potion()}")
    print(f"Strength potion: {strength_potion()}")

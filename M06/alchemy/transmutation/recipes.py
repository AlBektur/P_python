#!/opt/pyenv/shims/python


from ..elements import create_air  # relative import, by super parent
import alchemy  # absolute import accessing by points

# absolute import, importing directly the func
from elements import create_fire


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead toGold: brew ’{create_air()}’"
        f" and ’{alchemy.potions.strength_potion()}’ mixed with"
        f" ’{create_fire()}’"
        )


if __name__ == "__main__":
    print("\n===Testing how the module recipes works: ===\n\n")
    print(lead_to_gold())

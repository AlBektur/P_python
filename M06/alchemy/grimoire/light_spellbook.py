#!/opt/pyenv/shims/python


def light_spell_allowed_ingredients() -> list:
    return ['earth', 'air', 'fire', 'water']


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    if validate_ingredients(ingredients) == 'VALID':
        return (f"Spell recorded: {spell_name} ({ingredients}"
                f" - {validate_ingredients})")
    return (f"Spell recorded: {spell_name} ({ingredients}"
            f" - {validate_ingredients})")


if __name__ == "__main__":
    print("=== Testing light_spell_record() ===")

#!/opt/pyenv/shims/python


def validate_ingredients(ingredients: str) -> str:
    ingredients = ingredients.lower()
    from .light_spellbook import light_spell_allowed_ingredients
    data = light_spell_allowed_ingredients()
    for i in data:
        if i == ingredients:
            return 'VALID'
    return 'INVALID'

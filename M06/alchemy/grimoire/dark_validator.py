#!/opt/pyenv/shims/python

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients = ingredients.lower()
    data = dark_spell_allowed_ingredients()
    for i in data:
        if i == ingredients:
            return 'VALID'
    return 'INVALID'

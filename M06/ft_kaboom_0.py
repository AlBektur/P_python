#!/opt/pyenv/shims/python

from alchemy.grimoire import light_spell_record

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Testing record light spell: ")

    res = light_spell_record("fantasy", "fire")

    print(res)

#!/opt/pyenv/shims/python


if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    from alchemy.grimoire import dark_spell_record
    res = dark_spell_record("Black magic", "bats")

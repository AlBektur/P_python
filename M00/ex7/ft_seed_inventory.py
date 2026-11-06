def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    out: str = "flag"
    seed: str = seed_type.capitalize()

    if unit == "packets":
        out = f"{quantity} packets available"
    elif unit == "grams":
        out = f"{quantity} grams total"
    elif unit == "area":
        out = f"covers {quantity} square meters"
    else:
        print("Unknown unit type")
        return
    print(f"{seed} seeds: {out}")

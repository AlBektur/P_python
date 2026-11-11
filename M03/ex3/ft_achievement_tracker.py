#!/opt/pyenv/shims/python

import random


def gen_player_achievements() -> set:
    data = (
            'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
            'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
            'First Steps', 'Collector Supreme',
            'Untouchable', 'Sharp Mind', 'Boss Slayer'
        )

    res = set(random.sample(data, random.randint(0, 13)))

    return res


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    only_player_achievements: dict = {
        "Alice": {},
        "Bob": {},
        "Charlie": {},
        "Dylan": {}
    }

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    # This is instead of union
    all_achievements: set = alice | bob | charlie | dylan

    # This is instead of intersection new_set.intersection(set1, set2)
    common_achievements: set = alice & bob & charlie & dylan

    # This is instead of difference
    only_player_achievements["Alice"] = alice - bob - charlie - dylan
    only_player_achievements["Bob"] = bob - charlie - dylan - alice
    only_player_achievements["Charlie"] = charlie - dylan - alice - bob
    only_player_achievements["Dylan"] = dylan - alice - bob - charlie

    print()
    print(f"All distinct achievements: {all_achievements}\n")
    print(f"Common achievements: {common_achievements}\n")

    print(f"Only Alice has: {only_player_achievements['Alice']}")
    print(f"Only Bob has: {only_player_achievements['Bob']}")
    print(f"Only Charlie has: {only_player_achievements['Charlie']}")
    print(f"Only Dylan has: {only_player_achievements['Dylan']}\n")

    print(f"Alice is missing: {all_achievements - alice}")
    print(f"Bob is missing: {all_achievements - bob}")
    print(f"Charlie is missing: {all_achievements - charlie}")
    print(f"Dylan is missing: {all_achievements - dylan}")

#!/opt/pyenv/shims/python

import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    init_list: list = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
        ]
    init_dict = {key: random.randint(0, 1000) for key in init_list}

    cap_list: list = [x for x in init_list if x == x.capitalize()]
    all_cap_list: list = [x.capitalize() for x in init_list]

    dict_values = init_dict.values()
    average: float = round(sum(dict_values) / len(dict_values), 2)
    h_s: dict = {k: init_dict[k] for k in init_dict if init_dict[k] > average}

    print(f"Initial list of players: {init_list}")
    print(f"New list with all names capitalized: {all_cap_list}")
    print(f"New list of capitalized names only: {cap_list}")

    print(f"\nScore dict: {init_dict}")
    print(f"Score average is {average}")
    print(f"High scores: {h_s}")

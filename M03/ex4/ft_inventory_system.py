#!/opt/pyenv/shims/python

import sys


class InvalidParameter(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory = {}
    arguments = sys.argv[1:]

    for i in arguments:
        try:
            if ':' not in i:
                raise InvalidParameter(f"invalid parameter '{i}'")
            else:
                temp_list = i.split(':')
                if temp_list[0] not in inventory:
                    inventory[temp_list[0]] = int(temp_list[1])
                else:
                    print(f"Redundant item: '{temp_list[0]}' - discarding")
        except InvalidParameter as e:
            print(f"Error - {e}")
        except ValueError as e:
            print(f"Quantity error for 'key': {e}: 'value'")
    item_list: list = list(inventory.keys())
    total_quantity: int = len(item_list)
    total_elements: int = 0
    most: str = list(inventory.keys())[0]
    least: str = list(inventory.keys())[0]
    for k, v in inventory.items():
        total_elements += v
        if v > inventory[most]:
            most = k
        if v < inventory[least]:
            least = k

    print(f"Got inventory: {inventory}")
    print(f"Item list: {item_list}")
    print(f"Total quantity of the {total_quantity} items: {total_elements}")
    for k, v in inventory.items():
        percent = round((inventory[k] / total_elements) * 100, 1)
        print(f"Item {k} respresents {percent}%")
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")
    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")

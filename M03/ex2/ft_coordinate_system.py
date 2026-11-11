#!/opt/pyenv/shims/python
import math


class InvalidInput(Exception):
    pass


def get_player_pos() -> tuple:
    input_value = input("Enter new coordinates as floats in format 'x,y,z': ")
    xyz = input_value.split(',')

    try:
        if len(xyz) != 3:
            raise InvalidInput("Invalid syntax")
        cords = []
        for x in xyz:
            cords.append(float(x))
    except InvalidInput as e:
        print(e)
        return ()
    except ValueError:
        print(
            f"Error on parameter '{x}': "
            f"could not convert string to float: '{x}'"
            )
        return ()

    res = tuple(cords)
    return res


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")

    cord_1 = ()
    while not cord_1:
        cord_1 = get_player_pos()

    print(f"Got a first tuple: {cord_1}")
    x1, y1, z1 = cord_1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    res = math.sqrt((0-x1)**2 + (0-y1)**2 + (0-z1)**2)
    print(f"Distance to center: {round(res, 4)}")

    print("\nGet a second set of coordinates")
    cord_2 = ()
    while not cord_2:
        cord_2 = get_player_pos()
    x2, y2, z2 = cord_2

    res = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(res, 4)}")

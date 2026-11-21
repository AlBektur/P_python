#!/opt/pyenv/shims/python

from ex0.factory import FlameFactory, AquaFactory, CreatureFactory
from typing import Any


def testing_factory(Factory: CreatureFactory) -> None:
    print("Testing factory")

    if isinstance(Factory, FlameFactory):
        flameling = Factory.create_base('Flameling', 'fire')
        pyrodon = Factory.create_evolved('Pyrodon', 'fire/flying')

        print(flameling.describe())
        print(flameling.attack())

        print(pyrodon.describe())
        print(pyrodon.attack())

    if isinstance(Factory, AquaFactory):
        aquabub = a_factory.create_base('Aquabub', 'Water')
        torragon = a_factory.create_evolved('Torragon', 'Water')

        print(aquabub.describe())
        print(aquabub.attack())
        print(torragon.describe())
        print(torragon.attack())


def testing_battle(f1: Any, f2: Any) -> None:
    print("\nTesting battle")

    flameling = f1.create_base('Flameling', 'fire')
    aquabub = f2.create_base('Aquabub', 'water')
    print(flameling.describe())
    print('vs.')
    print(aquabub.describe())
    print('fight!')
    print(flameling.attack())
    print(aquabub.attack())


if __name__ == "__main__":

    f_factory = FlameFactory()
    a_factory = AquaFactory()

    testing_factory(f_factory)
    print()
    testing_factory(a_factory)
    print()
    testing_battle(f_factory, a_factory)

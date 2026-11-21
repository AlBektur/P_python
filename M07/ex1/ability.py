#!/opt/pyenv/shims/python


from abc import ABC, abstractmethod
from typing import Any
from ex0.creatures import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Any):
        return f"{target.name} heals itself and others for a large amount"


class TransformCapability(ABC):
    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass


# these two will be vailable throw HealingCreatureFactory in factory.py
class Sproutling(Creature, HealCapability):
    def __init__(self, name, cr_type) -> None:
        super().__init__(name, cr_type)

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def describe(self) -> str:
        return f"{self.name} is {self.cr_type} type Creature"

    def heal(self):
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name, cr_type) -> None:
        super().__init__(name, cr_type)

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def describe(self) -> str:
        return f"{self.name} is {self.cr_type} type Creature"

    def heal(self):
        return f"{self.name} heals itself and others for a large amount"


# these two will be available throw TransformCreatureFactory
class Shiftling(Creature, TransformCapability):
    def __init__(self, name, cr_type) -> None:
        super().__init__(name, cr_type)
        self.form = 'regular'

    def attack(self) -> str:
        if self.form == 'regular':
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def describe(self) -> str:
        return f"{self.name} is {self.cr_type} type Creature"

    def transform(self):
        print(f"{self.name} shifts into a sharper form")
        self.form = 'evolved'

    def revert(self):
        print("Shiftling returns to normal")
        self.form = 'regular'


class Morphagon(Creature, TransformCapability):
    def __init__(self, name, cr_type) -> None:
        self._form = 'regular'
        super().__init__(name, cr_type)

    def attack(self) -> str:
        if self._form == 'regular':
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def describe(self) -> str:
        return f"{self.name} is {self.cr_type} type Creature"

    def transform(self):
        print(f"{self.name} morphs into a dragonic battle form")
        self._form = 'evolved'

    def revert(self):
        print(f"{self.name} stabilizes its form.")
        self._form = 'regular'


if __name__ == "__main__":
    print('=== Test ability ===')

    test = Sproutling('test_name', 'test_type')
    test2 = Morphagon('no name', 'no type')
    test3 = Shiftling('test3', 'wood')
    print(test3.attack())
    test3.transform()
    print(test3.attack())

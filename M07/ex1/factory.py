#!/opt/pyenv/shims/python

from ex0 import CreatureFactory
from ex0.creatures import Creature
from .ability import Sproutling, Bloomelle
from .ability import Shiftling, Morphagon
from typing import Any

class HealingCreatureFactory(CreatureFactory):
    def create_base(self, creature: str, cr_type: str) -> Any:
        return Sproutling(creature, cr_type)

    def create_evolved(self, creature: str, cr_type: str) -> Any:
        return Bloomelle(creature, cr_type)


class TransformCreatureFactory(CreatureFactory):
    def create_base(self, creature: str, cr_type: str) -> Any:
        return Shiftling(creature, cr_type)

    def create_evolved(self, creature: str, cr_type: str) -> Any:
        return Morphagon(creature, cr_type)


if __name__ == "__main__":
    print("\n\n=== test ex1 factory ===")

    healing_cf = HealingCreatureFactory()
    transform_cf = TransformCreatureFactory()

#!/opt/pyenv/shims/python

from typing import Any
from ex0 import CreatureFactory
from .ability import Sproutling, Bloomelle
from .ability import Shiftling, Morphagon


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

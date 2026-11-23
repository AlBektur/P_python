#!/opt/pyenv/shims/python

from abc import ABC, abstractmethod
from .creatures import Flameling, Pyrodon, Aquabub, Torragon
from typing import Any


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self, creature: str, cr_type: str) -> Any:
        pass

    @abstractmethod
    def create_evolved(self, creature: str, cr_type: str) -> Any:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self, creature: str, cr_type: str) -> Any:
        return Flameling(creature, cr_type)

    def create_evolved(self, creature: str, cr_type: str) -> Any:
        return Pyrodon(creature, cr_type)


class AquaFactory(CreatureFactory):
    def create_base(self, creature: str, cr_type: str) -> Any:
        return Aquabub(creature, cr_type)

    def create_evolved(self, creature: str, cr_type: str) -> Any:
        return Torragon(creature, cr_type)

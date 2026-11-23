#!/opt/pyenv/shims/python

from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.ability import HealCapability, TransformCapability


class InvalidStrategy(Exception):
    def __init__(self, error_message: str) -> None:
        self.error_message = error_message


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategy(
                f"Invalid Creature '{creature.name}'"
                "for this aggressive strategy"
            )
        creature.transform()
        print(creature.attack())
        creature.revert()


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise InvalidStrategy(
                f"Invalid Creature '{creature.name}'"
                "for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())

#!/opt/pyenv/shims/python

from abc import ABC, abstractmethod

class  BattleStrategy(ABC):
    @abstractmethod
    def act():
        pass

    @abstractmethod
    def is_valid() -> bool:
        pass

class NormalStrategy(BattleStrategy):
    def act():
        pass

    def is_valid() -> bool:
        pass


class AggressiveStrategy(BattleStrategy):
    def act():
        pass

    def is_valid() -> bool:
        pass

class DefensiveStrategy(BattleStrategy):
    def act():
        pass

    def is_valid() -> bool:
        pass


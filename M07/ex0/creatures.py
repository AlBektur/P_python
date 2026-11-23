#!/opt/pyenv/shims/python

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, cr_type: str) -> None:
        self.name = name
        self.cr_type = cr_type

    @abstractmethod
    def attack(self) -> str:
        pass

    @abstractmethod
    def describe(self) -> str:
        pass


class Flameling(Creature):
    def __init__(self, name: str, cr_type: str) -> None:
        super().__init__(name, cr_type)

    def attack(self) -> str:
        return f"{self.name} uses Fire ball"

    def describe(self) -> str:
        return f"{self.name} is a {self.cr_type} type Creature"


class Pyrodon(Creature):
    def __init__(self, name: str, cr_type: str) -> None:
        super().__init__(name, cr_type)

    def attack(self) -> str:
        return f"{self.name} uses Promotheus"

    def describe(self) -> str:
        return f"{self.name} is a {self.cr_type} type Creature"


class Aquabub(Creature):
    def __init__(self, name: str, cr_type: str) -> None:
        super().__init__(name, cr_type)

    def attack(self) -> str:
        return f"{self.name} uses Water gun"

    def describe(self) -> str:
        return f"{self.name} is a{self.cr_type} type Creature"


class Torragon(Creature):
    def __init__(self, name: str, cr_type: str) -> None:
        super().__init__(name, cr_type)

    def attack(self) -> str:
        return f"{self.name} uses poison"

    def describe(self) -> str:
        return f"{self.name} is {self.cr_type} type Creature"

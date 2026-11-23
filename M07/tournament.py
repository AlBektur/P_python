# #!/opt/pyenv/shims/python

from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategy,
    NormalStrategy,
)
from ex2.strategy import BattleStrategy


def battle(
    opponents: list[tuple[CreatureFactory, str, str, BattleStrategy]],
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    fighters = []
    for factory, name, cr_type, strategy in opponents:
        creature = factory.create_base(name, cr_type)
        fighters.append((creature, strategy))

    try:
        for i in range(len(fighters)):
            for j in range(i + 1, len(fighters)):
                creature1, strategy1 = fighters[i]
                creature2, strategy2 = fighters[j]

                print("\n* Battle *")
                print(creature1.describe())
                print("vs.")
                print(creature2.describe())
                print("now fight!")

                strategy1.act(creature1)
                strategy2.act(creature2)

    except InvalidStrategy as error:
        print(f"Battle error, aborting tournament: {error}")


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    basic = [
        (FlameFactory(), "Flameling", "Fire", NormalStrategy()),
        (HealingCreatureFactory(), "Sproutling", "Grass", DefensiveStrategy()),
    ]
    battle(basic)

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    invalid = [
        (FlameFactory(), "Flameling", "Fire", AggressiveStrategy()),
        (HealingCreatureFactory(), "Sproutling", "Grass", DefensiveStrategy()),
    ]
    battle(invalid)

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), "
          "(Transform+Aggressive) ]")
    multiple = [
        (AquaFactory(), "Aquabub", "Water", NormalStrategy()),
        (HealingCreatureFactory(), "Sproutling", "Grass", DefensiveStrategy()),
        (
            TransformCreatureFactory(), "Shiftling", "Normal",
            AggressiveStrategy(),
        ),
    ]
    battle(multiple)

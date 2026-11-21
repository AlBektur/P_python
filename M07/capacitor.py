#!/opt/pyenv/shims/python

from ex1 import HealingCreatureFactory, TransformCreatureFactory
if __name__ == "__main__":
    print("Testing Creature with healing capability")

    print(" base:")
    HCF = HealingCreatureFactory()
    sp = HCF.create_base('Sproutling', 'Grass')
    print(sp.describe())
    print(sp.attack())
    print(sp.heal())

    print(" evolved:")
    bl = HCF.create_evolved('Bloomelle', 'Grass/Fairy')
    print(bl.describe())
    print(bl.attack())
    print(bl.heal())
    print()

    print("Testing Creature with transform capability")
    print(" base:")
    TCF = TransformCreatureFactory()
    sh = TCF.create_base('Shiftling', 'Normal')
    print(sh.describe())
    print(sh.attack())
    sh.transform()
    print(sh.attack())
    sh.revert()

    print(" evolved:")
    mr = TCF.create_evolved('Morphagon', 'Normal/Dragon')
    print(mr.describe())
    print(mr.attack())
    mr.transform()
    print(mr.attack())
    mr.revert()

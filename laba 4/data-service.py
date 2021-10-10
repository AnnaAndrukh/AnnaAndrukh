import pandas as pd
from dataclasses import dataclass


@dataclass
class TypeOfMainAssets:
    code: int
    name: str
    discount: float


@dataclass
class MoveOfMainAssets:
    code: int
    plan: str
    expected: float
    year: float


type_array = []
type_array.append(TypeOfMainAssets(1000, "Тканини", 4))
type_array.append(TypeOfMainAssets(2000, "Одяг та білизна", 7.5))
type_array.append(TypeOfMainAssets(3000, "Взуття", 7.5))
type_array.append(TypeOfMainAssets(4000, "Трикотаж", 7.5))
type_array.append(TypeOfMainAssets(5000, "Галантерея", 9.5))

move_array = []
move_array.append(MoveOfMainAssets(1000, 4340, 4420, 2013))
move_array.append(MoveOfMainAssets(2000, 6280, 6720, 2013))
move_array.append(MoveOfMainAssets(3000, 5260, 5854, 2013))
move_array.append(MoveOfMainAssets(4000, 3720, 3682, 2013))
move_array.append(MoveOfMainAssets(5000, 2410, 2694, 2013))
move_array.append(MoveOfMainAssets(1000, 4600, 4640, 2014))
move_array.append(MoveOfMainAssets(2000, 6800, 7400, 2014))
move_array.append(MoveOfMainAssets(3000, 6000, 6250, 2014))
move_array.append(MoveOfMainAssets(4000, 3800, 3850, 2014))
move_array.append(MoveOfMainAssets(5000, 2700, 3000, 2014))
move_array.append(MoveOfMainAssets(1000, 4700, 4625, 2015))
move_array.append(MoveOfMainAssets(2000, 6700, 6630, 2015))
move_array.append(MoveOfMainAssets(3000, 6700, 6500, 2015))
move_array.append(MoveOfMainAssets(4000, 4300, 4500, 2015))
move_array.append(MoveOfMainAssets(5000, 3500, 3590, 2015))


def printTypeOfMainAssets(typeOfMainAssets):
    '''printTypeOfMainAssets fuction prints("Довідник товарних груп")with names and values'''

    print("Код:{code}, Наіменування:{name}, Торгова скидка:{discount}"
          .format(code=typeOfMainAssets.code, name=typeOfMainAssets.name, discount=typeOfMainAssets.discount))


def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Товарообіг універмагу"
    with names and values'''

    print("Код:{code}, План:{plan}, Очікується:{expected}, Рік:{year}"
          .format(code=moveOfMainAssets.code, plan=moveOfMainAssets.plan, expected=moveOfMainAssets.expected,
                  year=moveOfMainAssets.year))


for data in type_array:
    printTypeOfMainAssets(data)

for data in move_array:
    printMoveOfMainAssets(data)

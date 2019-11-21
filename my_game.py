__author__ = 'ME !'
# The Game - Unit!
# для подготовки к написанию "игры" подготовьте класс Unit. под подготовкой я подразумеваю продумать структуру,
# атрибуты, методы, возможные взаимодействия между обьектами, параметры инстанцирования и т.д.
#
# у базового юнита должны быть:
# идентификатор (имя?)
# здоровье (численное значение)
# атака (численное значение)
# защита (численное значение)
# возможность атаковать другого юнита (метод)
# возможность защищаться от другого атаки другого юнита (метод) ?
#
# У вас уже есть Unit. Реализуйте следующее:
# возможность добавлять юниту оружие и доспехи. Это потребует отдельного класса отвечающего за объект амуниции.
# Одевание на юнита обьекта амуниции производит пересчет характеристик юнита ()
# создайте класс Битва, который принимает два юнита и реализует механику битвы - юниты поочередно атакуют друг-друга
# пока у одного из них не здоровье не станет 0
#
# *так модифицируйте метод атака у юнита, чтобы юнит наносил неодинаковый урон при каждом ударе.
# напимер randint(x,y) где x и y - показатели минимальной и максимальной атаки юнита (как создать или
# задать мин и макс показатели атаки - на ваше усмотрение).


from random import randint


class Fight:

    def __init__(self, unit1, unit2):
        if all([isinstance(unit1, Unit), isinstance(unit2, Unit)]):
            self.unit1 = unit1
            self.unit2 = unit2
        else:
            raise TypeError("Not valid type of data in")

    def to_fight(self):
        if all([self.unit1._health > 0, self.unit2._health > 0]):       # нет смысла начинать бой, если кто-то "устал"
            who_starts = randint(1, 10)                                 # кто начинает бой
            if who_starts % 2 != 0:
                while self.unit1._health > 0 and self.unit2._health > 0:
                    self.unit1.to_attack(unit_2)
                    if self.unit2._health <= 0:
                        print(f'{self.unit1._name} defeated {self.unit2._name} !!!')
                        break
                    self.unit2.to_attack(unit_1)
                    if self.unit1._health <= 0:
                        print(f'{self.unit2._name} defeated {self.unit1._name} !!!')
                        break
            else:
                while self.unit1._health > 0 and self.unit2._health > 0:
                    self.unit2.to_attack(unit_1)
                    if self.unit1._health <= 0:
                        print(f'{self.unit2._name} defeated {self.unit1._name} !!!')
                        break
                    self.unit1.to_attack(unit_2)
                    if self.unit2._health <= 0:
                        print(f'{self.unit1._name} defeated {self.unit2._name} !!!')
                        break
        else:
            print('battle is impossible due to the death of one unit')


class Unit:
    def __init__(self, name, health=100, attack=1, defence=0):
        if all([isinstance(name, str), isinstance(health, int), isinstance(attack, int), isinstance(defence, int)]):
            self._name = name
            self._health = health if health > 0 else 100
            self._attack = attack if attack >= 0 else 1
            self._defence = defence if defence >= 0 else 0
        else:
            raise TypeError("Not valid type of data in")

    equipment = None

    def __str__(self):
        if 'equipment' in self.__dict__:                            # если появился атрибут equipment
            self.__dict__['equipment'] = str(self.equipment)
        return str(self.__dict__)

    def to_attack(self, enemy):
        if isinstance(enemy, self.__class__):
            if self._health > 0:
                # loss = 0
                attack_power = randint(1, self._attack)                # генерируем силу атаки атакующего
                print(f"{self._name}'s attack power : {attack_power}")
                if enemy._defence < attack_power:
                    loss = attack_power - enemy._defence
                    enemy._health -= loss
                    print(f'{self._name} has done {loss} damages on the {enemy._name}')
                else:
                    enemy._health -= 1                    # защита сработала, но на мин единицу уменьшим жизнь
                    print(f"{enemy._name} has fought back the {self._name}’s attack ")
                print(self, enemy)                       # для поверки промежуточных данных(можно убрать)
            else:
                print(f'{self._name} cannot attack, {self._name} is dead')
        else:
            raise TypeError('Not valid type of data in')

    def to_equip(self, equipment):
        self.equipment = equipment
        if self.equipment.sword.startswith('iron'):
            self._defence += 10
        if self.equipment.sword.startswith('diamond'):
            self._defence += 20
        if self.equipment.sword.startswith('golden'):
            self._defence += 30


class Equipment:
    def __init__(self, kind):           #=(input('Choose kind of equipment iron/diamond/golden   :')).lower()):
        if any([kind.lower() == 'iron', kind.lower() == 'diamond', kind.lower() == 'golden']):
            self.sword = kind.lower() + '_sword'                           # меч  щит  шлем ботинки
            self.shield = kind.lower() + '_shield'
            self.helmet = kind.lower() + '_helmet'
            self.boots = kind.lower() + '_boots'
        else:
            raise TypeError("Not valid type of data in")

    def __str__(self):
        return str(self.__dict__)


unit_1 = Unit('Nick', 100, 100, 50)
unit_2 = Unit('Li', 100, 100, 50)

print(unit_1, unit_2)
print(unit_1.equipment, unit_2.equipment)
print(Unit.equipment)

equipment_1 = Equipment('IRon')
equipment_2 = Equipment('diamond')

unit_1.to_equip(equipment_1)
unit_2.to_equip(equipment_2)

print(unit_1, unit_2)
print(unit_1.equipment, unit_2.equipment)
print(Unit.equipment)


fight = Fight(unit_1, unit_2)
fight.to_fight()



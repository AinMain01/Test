class Hero:
    def __init__(self, name="", healf=100, damage=1, defense=0):
        self.name, self.healf, self.damage, self.defense = name, healf, damage, defense

    def get_status(self):
        print(f"Имя: {self.name} \nЗдоровье: {self.healf} \nУрон: {self.damage} \nЗащита: {self.defense}")
        print("______________________________________")

    def increase_defense(self):
        if self.defense *1.5 < 100: self.defense *= 1.5
        else: self.defense = 100
        print(f"Текущий уровень защиты: {self.defense}")
        print("______________________________________")

    def make_damage(self, enemy):
        print(f"Атака по персонажу {enemy.name}!")
        print("______________________________________")
        enemy.get_damage(self.damage)

    def get_damage(self, damage):
        final_damage = damage - (damage * self.defense // 100)
        print(f"По герою {self.name} нанесён урон {final_damage}")
        self.healf -= final_damage
        print("______________________________________")

# hero_1 = Hero(name="Артур", damage=20, defense=5)
# hero_2 = Hero("Робин", 80, 30, 4)
# hero_1.get_status()
# hero_1.increase_defense()

# hero_2.get_status()
# hero_2.make_damage(hero_1)
# hero_1.get_status()

from random import randint as rd

class Archer:
    def __init__(self, name="", healf=100, damage=1, metcost=0.1, lovk=1):
        self.name, self.healf, self.damage, self.metcost, self.lovk = name, healf, damage, metcost, lovk

    def get_status(self):
        print(f"Имя: {self.name} \nЗдоровье: {self.healf} \nУрон: {self.damage} \nМеткость: {self.metcost} \nЛовкость: {self.lovk}")
        print("______________________________________")

    def level_up(self):
        self.healf += 10
        self.damage +=6
        if self.metcost +0.05 < 2:
            self.metcost += 0.05
        else:
            print(f"Достигнут лимит Меткости: {self.metcost}!")
            print("______________________________________")

        if self.lovk +2 < 25:
            self.lovk += 2
        else:
            print(f"Достигнут лимит Ловкости: {self.lovk}!")
            print("______________________________________")
        print("Левел повышен!")
        print("______________________________________")

    def make_damage(self, enemy):
        print(f"Атака по персонажу {enemy.name}!")
        print("______________________________________")
        enemy.get_damage(self.damage *self.metcost)
    
    def get_damage(self, damage):
        chance_damage = rd(1, 100)
        if self.lovk >= chance_damage: print(f"Лучник {self.name} увернулся от удара!")
        else:
            print(f"По герою {self.name} нанесён урон {damage}!")
            self.healf -= damage
        print("______________________________________")

archer_1 = Archer(name="Артур", damage=5, metcost=0.06)
archer_2 = Archer("Робин", 80, 30, 2, 25)
archer_2.get_status()
# archer_1.level_up()
# archer_1.get_status()

archer_1.make_damage(archer_2)
archer_2.get_status()
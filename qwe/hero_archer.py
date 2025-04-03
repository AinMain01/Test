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

import random

class Archer:
    def __init__(self, name="", healf=100, damage=1, metcost=0.1, lovk=1):
        self.name, self.healf, self.damage, self.metcost, self.lovk = name, healf, damage, metcost, lovk

    def get_status(self):
        print(f"Имя: {self.name} \nЗдоровье: {self.healf} \nУрон: {self.damage} \nМеткость: {self.metcost} \nЛовкость: {self.lovk}")
        print("______________________________________")

    def level_up(self):
        if self.metcost +0.05 > 2:
            self.metcost = 2
            self.healf += 10
            self.damage +=6
            print(f"Достигнут лимит Меткости: {self.metcost}!")
            print("Левел повышен!")
            print("______________________________________")
        elif self.lovk +2 > 25:
            self.lovk = 25
            self.healf += 10
            self.damage +=6
            print(f"Достигнут лимит Ловкости: {self.lovk}!")
            print("Левел повышен!")
            print("______________________________________")
        else:
            self.healf += 10
            self.damage +=6
            self.metcost += 0.05
            self.lovk += 2
            print("Левел повышен!")
            print("______________________________________")

    def make_damage(self, enemy):
        print(f"Атака по персонажу {enemy.name}!")
        print("______________________________________")
        enemy.get_damage(self.damage)
    
    def get_damage(self, lovk):
        

        print(f"По герою {self.name} нанесён урон {final_damage}")
        self.healf -= final_damage
        print("______________________________________")

from random import randint

class Human:
    def __init__(self, name="", health=100):
        self._name, self._health = name, health

    def attack(self, enemy=""):
        damage = randint(1, 10)
        print(f"{self._name} наносит персонажу {enemy._name} {damage} урона!")
        enemy.get_damage(damage)

    def get_damage(self, damage=1):
        self._health -= damage
        print(f"{self._name} получает {damage} урона! Текущее здоровье - {self._health}.")

    def healing(self):
        healing = randint(5, 15)
        self._health += healing
        print(f"{self._name} восстанавливает {healing} здоровья. Текущее здоровье - {self._health}")


class Warrior(Human):
    def __init__(self, name="", health=100, defense=0):
        super().__init__(name, health)
        self._defense = defense

    def attack(self, enemy=""):
        damage =randint(10, 20)
        print(f"{self._name} наносит персонажу {enemy._name} {damage} урона!")
        enemy.get_damage(damage)
    
    def get_damage(self, damage=1):
        finish_damage = max(0, damage - self._defense)
        super().get_damage(finish_damage)


class Archer(Human):
    def __init__(self, name="", health=100, accuracy=0.0, agility=0):
        super().__init__(name, health)
        self._accuracy, self._agility = accuracy, agility

    def attack(self, enemy=""):
        base_damage = randint(15, 25)
        damage = base_damage * self._accuracy
        print(f"{self._name} наносит персонажу {enemy._name} {damage} урона!")
        enemy.get_damage(damage)

    def get_damage(self, damage=1):
        if randint(1, 100) <= self._agility: print(f"{self._name} увернулся от удара!")
        else: super().get_damage(damage)
        
    
human = Human("Стив", 80)
warrior = Warrior("Артур", 120, 5)
archer = Archer("Робин", 90, 1.15, 10)

human.attack(warrior)
warrior.attack(archer)
archer.healing()
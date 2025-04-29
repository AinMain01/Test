from random import randint
class Human:
    def __init__(self, name="", health=100):
        self._name, self._health = name, health

    def attack(self, enemy):
        print(f"{self._name} наносит персонажу {enemy} {enemy.get_damage()} урона!")
        enemy.get_damage(self.damage)

    def get_damage(self, damage=randint(1, 10)):
        self._health -= damage
        print(f"{self._name} получает {damage} урона! Текущее здоровье - {self._health}.")

    def healing(self):
        healing = randint(5, 15)
        self._health += healing
        print(f"{self._name} восстанавливает {healing} здоровья. Текущее здоровье - {self._health}")

class Warrior(Human):
    def __init__(self, name, health, defense=0):
        super().__init__(name, health)
        self._defense = defense
    
    def get_damage(self):
        super().get_damage()
        damage = randint(10, 20)
        if damage - self._defense < 0: damage = 0
        else: damage -= self._defense

class Archer(Human):
    def __init__(self, name, health, accuracy=0.0, agility=0):
        super().__init__(name, health)
        self._accuracy, self._agility = accuracy, agility

    def get_damage(self):
        super().get_damage()
        damage = randint(15, 25) * self._accuracy
        
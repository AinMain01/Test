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

hero_1 = Hero(name="Артур", damage=20, defense=5)
hero_2 = Hero("Робин", 80, 30, 4)
hero_1.get_status()
hero_1.increase_defense()

hero_2.get_status()
hero_2.make_damage(hero_1)
hero_1.get_status()
class Base_Human:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def introduce(self):
        print(f"Привет, меня зовут {self.name} \nМой возраст {self.age}")

    def walk(self):
        print(f"{self.name} идёт на прогулку")

class Programer(Base_Human):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language

    def coding(self):
        print(f"Программист {self.name} сейчас пишет код!")

class Backend_Programer(Programer):
    pass

human = Base_Human("Миша", 25)
proger = Programer("Дима", 26, "Python")
back_proger = Backend_Programer("Иван", 27, "C++")
human.introduce()
proger.introduce()
print(f"{human.__dict__} \n{proger.__dict__} \n{back_proger.__dict__}")
# proger.coding()
# human.coding()
back_proger.walk()
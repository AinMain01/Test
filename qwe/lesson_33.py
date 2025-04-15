class Dog:
    def __init__(self, name="", happiness=0):
        self.__name, self.__happiness = name, happiness
    
    def carres(self):
        self.__happiness += 10
        print("Гав-Гав!")

    def set_name(self, new_name=""):
        if any(new_name) == True:
            self.__name = new_name
            print(f"Теперь собаку зовут {self.__name}!")
        else: print("В имени собаки должны быть только буквы!")

    def get_name(self): print(f"Собаку зовут: {self.__name}")

    def bring_item(self, item="", distance=0):
        if distance <= 100 and self.__happiness >= 10: print(f"{self.__name.capitalize()} принёс(ла) предмет: {item}")
        elif distance > 100: print(f"{item.capitalize()} находится слишком далеко!")
        elif self.__happiness < 10: print(f"{self.__name.capitalize()} нуждается в вашей заботе!")

Lucky = Dog("Шарик")
Lucky.carres()
Lucky.bring_item("палка", 20)
Lucky.set_name("Бобик")
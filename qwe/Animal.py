class Animal:
    def __init__(self, name="", habitan=""):
        self._name, self._habitan = name, habitan

    def introduse(self):
        print(f"Привет, меня зовут {self._name} \nМоя среда обитания - {self._habitan}")

class Tiger(Animal):
    def __init__(self, name, habitan, color=""):
        super().__init__(name, habitan)
        self._color = color

    def show_color(self):
        print(f"Окрас тигра по имени {self._name}: {self._color}")

class Elephant(Animal):
    def __init__(self, name, habitan, tusk_lenght=0):
        super().__init__(name, habitan)
        self._tusk_lenght = tusk_lenght
    
    def show_tusks(self):
        print(f"У слона по имени {self._name} есть бивни длиной {self._tusk_lenght} см.")

    
new_tiger = Tiger("Полосатик", "Джунгли", "оранжевый")
new_elephant = Elephant("Элли", "Саванна", 200)
new_tiger.introduse()
new_tiger.show_color()
new_elephant.introduse()
new_elephant.show_tusks()
class Capitane:
    __cap = None
    def __new__(cls, *args, **kwargs):
        if cls.__cap is None: cls.__cap = super().__new__(cls)
        return cls.__cap

    def __init__(self, name, age, height, weight):
        self.name, self. age, self.height, self.weight = name, age, height, weight

cap = Capitane("Дима", 43, height=174, weight=75)
new_cap = Capitane("Артём", 16, height=167, weight=57)
# print(f"{cap.__dict__} \n{new_cap.__dict__}")


class Car:
    def __init__(self, model):
        self.model = model

    # def __str__(self):
    #     return f"Модель машины: {self.model}"
    
    def __repr__(self):
        return f"Car({self.model})"
    

my_car = Car("Camry")
print(my_car)
class Car:
    def __new__(cls, *args, **kwargs):
        print(f"Работант метод __new__() для класса {cls} \n{args} \n{kwargs}")
        return super().__new__(cls)

    def __init__(self, color, model, speed=0):
        self.color, self.model, self.speed = color, model, speed

my_car = Car(color="Белый", model="Camry", speed=100)
print(my_car)
class Car:
    def __init__(self, mark="", model="", color="", speed=0):
        print("Работает метод __init__")
        self.mark = mark
        self.model = model
        self.color = color
        self.speed = speed

    def __del__(self):
        print("Сработал метод __del__")

    def set_engine(self, power_engine):
        self.power_engine = power_engine

    def show_info(self):
        print(f"Марка автомобиля: {self.mark}")
        print(f"Модель автомобиля: {self.model}")
        print(f"Цвет автомобиля: {self.color}")
        print(f"Скорость автомобиля: {self.speed}")

    def get_params(self):
        return (self.mark, self.model, self.color, self.speed)

my_car_1 = Car("Nisan", "Jude", "red", 0)
my_car_2 = Car()

# print(my_car_2.get_params())
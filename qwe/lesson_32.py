class Square():
    def __init__(self, side_lenght): self.side_lenght = side_lenght

    def area(self):
        return (self.side_lenght**2)

side_lenght = int(input("Введите длину стороны квадрата: "))
figure = Square(side_lenght)
print(figure.area())
class Rectanagle:
    def __init__(self, lenght, width):
        self._lenght, self._widht = lenght, width
    
    def get_area(self):
        return self._lenght * self._widht
    
    def get_perimeter(self):
        return (self._lenght + self._widht) * 2

class Triangle:
    def __init__(self, site_1, site_2, site_3):
        self._site_1, self._site_2, self._site_3 = site_1, site_2, site_3

    def get_area(self):
        p = (self._site_1 + self._site_2 + self._site_3) / 2
        return (p * (p-self._site_1) * (p-self._site_2) * (p-self._site_3))**0.5
    
    def get_perimeter(self):
        return self._site_1 + self._site_2 + self._site_3
    
rect_1 = Rectanagle(4, 5)
# rect_2 = Rectanagle(8, 10)
trian_1 = Triangle(3, 4, 5)
# trian_2 = Triangle(3, 5)

# print(f"{rect_1.get_area()} \n{rect_2.get_area()}")
# print(f"{trian_1.get_area()} \n{trian_2.get_area()}")

figures = [rect_1, trian_1]
for fig in figures:
    print(f"Площадь фигуры: {fig.get_area()} \nПериметр фигуры: {fig.get_perimeter()}")
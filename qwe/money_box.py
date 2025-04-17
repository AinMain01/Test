class Money_box:
    def __init__(self, money=0):
        self.__money = money

    def __repr__(self):
        return f"{self.__money}"
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Money_box(self.__money + other)
        else: print("Некорректное сложение!")
    
    def __radd__(self, other):
        return Money_box(self.__add__(other))
    
box = Money_box(123)
box += 10
print(box)


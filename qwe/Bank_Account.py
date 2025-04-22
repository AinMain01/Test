class Bank_Account:
    def __init__(self, balance=0):
        self.__balance = balance

    def __repr__(self):
        return f"Bank Account({self.__balance})"
    
    def __add__(self, other):
        if isinstance(other, (int, float)): return Bank_Account(self.__balance + other)
        else: print("Некорректное пополнение счёта")
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            if self.__balance - other >= 0: return Bank_Account(self.__balance - other)
            else: print("Баланс не может стать отрицательным!")
        else: print("Некорректное списание средств со счёта")
    
my_acc = Bank_Account(10000)
my_acc = my_acc + 1000.123
print(my_acc)
my_acc = 200 + my_acc
print(my_acc)
my_acc = my_acc - 5000
print(my_acc)
my_acc = my_acc - 10000
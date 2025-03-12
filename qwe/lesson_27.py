n = list(set(map(int, input("Введите числа на карточках: ").split())))
sacha, peta = 0, 0
def summa(n):
    maxi = max([n[0], n[-1]])
    n.remove(maxi)
    return maxi
for i in range(len(n) // 2 +1):
    if len(n) >= 2:
        sacha += summa(n)
        peta += summa(n)
    else: sacha += n[0]
print(sacha, peta)
if sacha > peta: print("Саша")
elif sacha < peta: print("Петя")
else: print("Ничья!")
n = int(input())
list = []
for i in range(n): list.append(int(input()))

def summa(list):
    if len(list) != 1:
        maxi = max([list[0], list[-1]])
        list.remove(maxi)
        return maxi
    else:
        maxi = max(list)
        return maxi

Sacha = 0
Peta = 0

for x in list:
    Sacha += summa(list)
    Peta += summa(list)


print(Sacha, Peta)
if Sacha > Peta: print("Саша")
elif Peta > Sacha: print("Петя")
else: print("Ничья!")
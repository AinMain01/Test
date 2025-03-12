n = int(input("Введите кол-во карточек: "))
cards = list(map(int, input("Введите числа: ").split()))
sasha, peta = 0, 0
left, right = 0, n - 1

for xod in range(n):
    if cards[left] > cards[right]:
        if xod % 2 == 0: sasha += cards[left]
        else: peta += cards[left]
        left += 1
    else:
        if xod % 2 == 0: sasha += cards[right]
        else: peta += cards[right]
        right -= 1

print(sasha, peta)
if sasha > peta: print("Саша")
elif peta > sasha: print("Петя")
else: print("Ничья!")

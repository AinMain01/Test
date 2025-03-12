n = int(input("Введите кол-во дней наблюдения: "))
data = [x for _ in range(n) if (x := int(input("Введите температуру: "))) >= 0]
print(sum(data) / len(data), len(data), sep='\n')
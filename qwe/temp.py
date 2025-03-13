n = int(input("Введите кол-во дней наблюдения: "))
data = [x for i in range(n) if (x := int(input("Введите температуру: "))) >= 0]
print(f"Средняя положительная температура: {sum(data) / len(data)}")
print(f"Кол-во дней с положительной температурой: {len(data)}")
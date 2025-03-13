n = int(input("Введите кол-во строк: "))
kol_words = {}

for i in range(n):
    words = input("Введите строку: ").lower().split()
    for word in words:
        if word in kol_words:
            kol_words[word] += 1
        else:
            kol_words[word] = 1

camoe_words = max(kol_words, key=kol_words.get)
kol_vo = kol_words[camoe_words]

print(f"Самое часто повторяющееся слово: {camoe_words}")
print(f"Кол-во повторов: {kol_vo}")
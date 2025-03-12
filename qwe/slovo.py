n = int(input())
kol_words = {}

for i in range(n):
    words = input().lower().split()
    for word in words:
        if word in kol_words:
            kol_words[word] += 1
        else:
            kol_words[word] = 1

camoe_words = max(kol_words, key=kol_words.get)
kol_vo = kol_words[camoe_words]

print(camoe_words)
print(kol_vo)
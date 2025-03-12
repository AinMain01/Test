n = [x for _ in range(int(input("Введите t (1<=t<=20): "))) if ((x := int(input("Введите число n (1<=n<=109): "))))]
for a in n: print(len(sorted(list(set([x for i in range(1, int(a**0.5) +2) for x in (i**2, i**3) if x <= a])))))
# a = int(input())
# print(sorted(list(set([x for i in range(1, int(a**0.5) +2) for x in (i**2, i**3) if x <= a]))))
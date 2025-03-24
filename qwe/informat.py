n = int(input())
sumi = 0
for i in range(n):
    a = int(input())
    if a % 10 == 4:
        sumi += a
print(sumi)
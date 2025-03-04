n = int(input("Введите число строк: "))
packal_tr = []
for line in range(n):
    now_line = []
    for num in range(line + 1):
        if num == 0 or num == line:
            now_line.append(1)
        else:
            now_line.append(packal_tr[line -1][num -1] + packal_tr[line - 1][num])
    packal_tr.append(now_line)

print_tr = len(' '.join(map(str, packal_tr[-1])))
for line in packal_tr:
    print(' '.join(map(str, line)).center(print_tr))
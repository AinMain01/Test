name = input("Укажите своё имя: ")
file = open("log_calc.txt", "a", encoding="UTF-8")
file.write(f"Пользователь: {name}\n")
while True:
    try:
        num_1 = int(input("Введите 1-е число: "))
        oper = input("Введите операцию (+ - * / // %): ")
        num_2 = int(input("Введите 2-е число: "))
        file.write(f"Совершается операция: {num_1} {oper} {num_2}\n")
        rezult = eval(f"{num_1} {oper} {num_2}")
    except ZeroDivisionError:
        num_2 = int(input("Ошибка деления на ноль! Введите новое число: "))
        file.write(f"Ошибка деления на ноль\n")
        file.write(f"Введено новое число: {num_2}\n")
    except ValueError:
        print("Введены некоректные значения!")
        num_1 = int(input("Введите 1-е число: "))
        num_2 = int(input("Введите 2-е число: "))
        file.write(f"Ввод некоректных значения\n")
        file.write(f"Введены новые числа: {num_1} и {num_2}\n")
    except SyntaxError:
        oper = input("Введите конкретную операцию (+ - * / // %): ")
        file.write(f"Ввод некоректной операции\n")
        file.write(f"Введена новая операция: {oper}\n")
    finally:
        rezult = eval(f"{num_1} {oper} {num_2}")
        print(f"Результат операции ({num_1} {oper} {num_2}): {rezult}")
        file.write((f"Результат операции ({num_1} {oper} {num_2}): {rezult}\n"))
        is_continion = input("Продолжить работу с калькулятором? (Да/Нет): ")
        if is_continion.lower() == "нет":
            print("Досвидания!")
            file.write(f"-----------------------------------------------------------------\n")
            file.close()
            break
        print(f"---------------------------------------------")
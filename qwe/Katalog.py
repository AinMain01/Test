katalog = {}

while True:
    print("Список возможных действий:")
    print("1 - Добавить новую книгу")
    print("2 - Поиск книги по названию")
    print("3 - Удалить книгу из каталога")
    print("4 - Показать список книг")
    print("0 - Закончить работу")

    user_choice = int(input("Выберете действие: "))
    if user_choice == 0:
        print("До свидания!")
        break
    elif user_choice == 1:
        title = input("Введите название книги: ")
        while title in katalog:
            title = input("Такая книга уже есть. Введите другое назвакние: ")
        auther = input("Введите автора: ")
        katalog[title] = auther
        print("Книга успешно добавлена!")
    elif user_choice == 2:
        title = input("Введите название книги: ")
        if title in katalog:
            print("Информация о книге: ")
            print("Название:", title)
            print("Автор:", katalog[title])
        else: print("Книга не найдена")
    elif user_choice == 3:
        title = input("Введите название книги: ")
        if title in katalog:
            del katalog[title]
            print("Книга удалена из каталога")
        else: print("Книга не найдена")
    elif user_choice == 4:
        print("Информация о книгах в каталоге:")
        if katalog:
            for book in katalog:
                print(f"Название: {book}, Автор: {katalog[book]}")
        else: print("Каталог пуст!")
    else:
        print("Выбрано неверное действие. Попробуйте ещё раз: ")
    print("__________________________________________________________")
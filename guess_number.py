from tkinter import * 
from random import randint

class Game:
    def __init__(self):
        self.attempt = 0

    def move_result(self, user_choice):
        pc_choice = randint(1, 100)

        try:
            if user_choice > 100 or user_choice < 1:
                return f"Введите число от 1 до 100 вклюительно!"
            elif user_choice == pc_choice:
                self.attempt += 1
                return f"Ваше число - {user_choice}. Вы угадали!"
            elif user_choice < pc_choice:
                self.attempt += 1
                return f"Ваше число - {user_choice}. Моё число больше!"
            elif user_choice > pc_choice:
                self.attempt += 1
                return f"Ваше число - {user_choice}. Моё число меньше!"
        except ValueError:
            return f"Введите корректное число!"
        else: return f"Неизвестная ошибка!"
        
    def show_info(self):
        return f"Попыток - {self.attempt}"

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Угадай число")
        self.window.geometry("400x500")
        self.game = Game()
        self.start_UI(self.window)
        self.window.mainloop()

    def start_UI(self, window):
        for c in range(4): window.columnconfigure(index=c, weight=2)
        for r in range(3): window.rowconfigure(index=r, weight=1)

        self.lb_1 = Label(window, text="Угадай число от 1 до 100:", font=("Arial", 20))
        self.lb_1.grid(row=0, column=0, columnspan=3)

        self.lb_2 = Label(window, text=self.game.show_info() ,font=("Arial", 13))
        self.lb_2.grid(row=1, column=0)

        self.lb_3 = Label(window, text="Сначала введите число", font=("Arial", 13))
        self.lb_3.grid(row=4, column=0)

        self.button = Button(window, text="Проверить", font=("Arial", 15), command=lambda: self.button_click(self.user))
        self.button.grid(row=3, column=0)

        self.user = Entry(width=10)
        self.user.grid(row=2, column=0)

    def button_click(self, user_choice):
        self.lb_3["text"] = self.game.move_result(user_choice)
        self.lb_2["text"] = self.game.show_info()

app = GUI()
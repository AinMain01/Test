from tkinter import * 
from random import randint

class Game:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.pc_choice = randint(1, 100)
        self.attempt = 0
        print(self.pc_choice)

    def move_result(self, user_choice):
        try:
            val = user_choice.get()

            if int(val) > 100 or int(val) < 1:
                return "Введите число от 1 до 100 вклюительно!"
            elif int(val) == self.pc_choice:
                self.attempt += 1
                n = self.attempt
                self.reset_game()
                return f"Ваше число - {val}. Вы угадали за {n} попыток!"
            if int(val) < self.pc_choice:
                self.attempt += 1
                return f"Ваше число - {val}. Моё число больше!"
            elif int(val) > self.pc_choice:
                self.attempt += 1
                return f"Ваше число - {val}. Моё число меньше!"
        except ValueError: return f"Введите корректное число!"
        
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
        for c in range(4): window.columnconfigure(index=c, weight=1)
        for r in range(3): window.rowconfigure(index=r, weight=1)

        self.lb_1 = Label(window, text="Угадай число от 1 до 100:", font=("Arial", 20))
        self.lb_1.grid(row=0, column=0, columnspan=3)

        self.lb_2 = Label(window, text=self.game.show_info() ,font=("Arial", 13))
        self.lb_2.grid(row=0, column=0, columnspan=3, rowspan=2)

        self.lb_3 = Label(window, text="Сначала введите число", font=("Arial", 13))
        self.lb_3.grid(row=2, column=0, columnspan=3)

        self.button = Button(window, text="Проверить", font=("Arial", 15), command=lambda: self.button_click(self.user))
        self.button.grid(row=1, column=0, columnspan=3, rowspan=2)

        self.user = Entry(width=10)
        self.user.grid(row=1, column=0, columnspan=3)

    def button_click(self, user_choice):
        self.lb_3["text"] = self.game.move_result(user_choice)
        self.lb_2["text"] = self.game.show_info()

app = GUI()
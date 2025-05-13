from random import choice
from tkinter import Tk, Button, Label

class Game:
    def __init__(self):
        self.win, self.lose, self.draw, self.moves = 0, 0, 0, ["Камень", "Ножницы", "Бумага"]

    def move_result(self, user_choice):
        pc_choice = choice(self.moves)
        if user_choice == pc_choice:
            self.draw += 1
            return f"Ход игрока: {user_choice}\nХод компьютера: {pc_choice}\nНичья!"
        elif user_choice == "Камень" and pc_choice == "Ножницы" or user_choice == "Ножницы" and pc_choice == "Бумага" or user_choice == "Бумага" and pc_choice == "Камень":
            self.win += 1
            return f"Ход игрока: {user_choice}\nХод компьютера: {pc_choice}\nПобеда!"
        else:
            self.lose += 1
            return f"Ход игрока: {user_choice}\nХод компьютера: {pc_choice}\nПроигрыш!"
        
    def show_info(self):
        return f"Победы: {self.win}\nПроигрыши: {self.lose}\nНичьи: {self.draw}"


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Камень ножницы бумага")
        self.window.geometry("500x300")
        self.game = Game()
        self.start_UI(self.window)
        self.window.mainloop()

    def start_UI(self, window):
        for c in range(3): window.columnconfigure(index=c, weight=1)
        for r in range(3):window.rowconfigure(index=r, weight=1)

        self.button_1 = Button(window,text="Камень", font=("Arial", 15), command=lambda: self.button_click("Камень"))
        self.button_2 = Button(window,text="Ножницы", font=("Arial", 15), command=lambda: self.button_click("Ножницы"))
        self.button_3 = Button(window,text="Бумага", font=("Arial", 15), command=lambda: self.button_click("Бумага"))

        self.button_1.grid(row=2, column=0)
        self.button_2.grid(row=2, column=1)
        self.button_3.grid(row=2, column=2)

        self.lb_1 = Label(window, text="Начало игры!", font=("Arial", 20))
        self.lb_1.grid(row=1, column=0, columnspan=3)

        self.lb_2 = Label(window, justify="left", text=self.game.show_info() ,font=("Arial", 13))
        self.lb_2.grid(row=0, column=0)

    def button_click(self, user_choice):
        self.lb_1["text"] = self.game.move_result(user_choice)
        self.lb_2["text"] = self.game.show_info()

app = GUI()
from tkinter import *
from random import randint

class GuessGame:
    def init(self):
        self.reset_game()
        
    def reset_game(self):
        self.secret_number = randint(1, 100)
        self.attempts = 0
        
    def check_guess(self, number):
        try:
            num = int(number)
            self.attempts += 1
            
            if num < self.secret_number:
                return "Загаданное число больше!", False
            elif num > self.secret_number:
                return "Загаданное число меньше!", False
            else:
                message = f"Вы угадали за {self.attempts} попыток!"
                self.reset_game()
                return message, True
        except ValueError:
            return "Ошибка! Введите целое число.", False

class GuessingGUI:
    def init(self):
        self.window = Tk()
        self.window.title("Угадай число")
        self.window.geometry("400x200")
        self.game = GuessGame()
        self.create_ui()
        self.window.mainloop()
        
    def create_ui(self):
        for col in range(2): self.window.columnconfigure(index=col, weight=1)
        for row in range(4): self.window.rowconfigure(index=row, weight=1)
        
        self.title_label = Label(self.window, text="Введите число от 1 до 100:", font=("Arial", 14))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.entry = Entry(self.window, font=("Arial", 12))
        self.entry.grid(row=1, column=0, columnspan=2, padx=10, sticky="ew")
        
        self.check_btn = Button(self.window, text="Проверить", font=("Arial", 12), command=self.check_number)
        self.check_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result_label = Label(self.window, text="", font=("Arial", 12), fg="blue")
        self.result_label.grid(row=3, column=0, columnspan=2)
        
        self.window.bind('<Return>', lambda event: self.check_number())
        
    def check_number(self):
        user_input = self.entry.get()
        result, is_win = self.game.check_guess(user_input)
        self.result_label.config(text=result)
        
        if is_win:
            self.result_label.config(fg="green")
        else:
            self.result_label.config(fg="blue")
            
        self.entry.delete(0, END)

if __name__ == "__main__":
    app = GuessingGUI()
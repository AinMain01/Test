from customtkinter import *

class Main_Window(CTk):
    def __init__(self):
        super().__init__()
        self.title("Цвета и фигуры")
        self.geometry("400x300")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.button = CTkButton(self, text="Отправить", command=self.show_info)
        self.button.grid(row=1, padx=10, pady=10, sticky="ew", columnspan=2)
        self.text = CTkLabel(self, text="")
        self.text.grid(row=2, padx=10, pady=10, sticky="ew", columnspan=2)
        self.checkbox_frame = My_checkbox_Frame(self, title="Выбери цвет", values=("Красный", "Синий", "Зелёный"))
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.radiobtton_frame = My_Radiobutton_Frame(self, title="Выбери фигуру", values=("Круг", "Квадрат"))
        self.radiobtton_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    def show_info(self):
        self.text.configure(text=f"Цвета: {self.checkbox_frame.get()}\nФигура: {self.radiobtton_frame.get()}")


class My_checkbox_Frame(CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.checkboxes = []
        self.title = CTkLabel(self, text=title, fg_color="grey", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        for i in range(len(values)):
            checkbox = CTkCheckBox(self, text=values[i])
            checkbox.grid(row=i+1, column=0, padx=10, pady=10, sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1: checked_checkboxes.append(checkbox.cget("text"))
        return ", ".join(checked_checkboxes)


class My_Radiobutton_Frame(CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.figure = StringVar()
        self.title = CTkLabel(self, text=title, fg_color="grey", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        for i in range(len(values)):
            radiobutton = CTkRadioButton(self, text=values[i], value=values[i], variable=self.figure)
            radiobutton.grid(row=i+1, column=0, padx=10, pady=10, sticky="w")

    def get(self):
        return self.figure.get()


window = Main_Window()
window.mainloop()
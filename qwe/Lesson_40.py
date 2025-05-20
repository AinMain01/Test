from customtkinter import *

def button_click():
    global count_clicks
    count_clicks += 1
    clicks.configure(text=f"Колличество нажатий: {count_clicks}")

window = CTk()
window.title("Моё окно")
window.geometry("400x300")
window.config(bg="gray")

window.grid_columnconfigure((0), weight=1)
window.grid_rowconfigure((0, 1, 2, 3), weight=1)

label = CTkLabel(window, text="Пример текста в Custom Tkinter", bg_color="gray")
label.grid(row=0, column=0)
label.cget('font').configure(size=20)

count_clicks = 0
clicks = CTkLabel(window, text=f"Колличество нажатий: {count_clicks}", bg_color="gray")
clicks.grid(row=1, column=0)

button = CTkButton(window, text="Кнопка", fg_color="blue", command=button_click, bg_color="gray")
button.grid(row=2, column=0, padx=20, pady=20, sticky="we")

checbox_frame = CTkFrame(window)
checbox_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nswe")
checbox_frame.grid_columnconfigure((0, 1), weight=1)
checbox_frame.grid_rowconfigure((0), weight=1)
chekbox_1 = CTkCheckBox(checbox_frame, text="Вариант 1")
chekbox_1.grid(row=0, column=0)
chekbox_2 = CTkCheckBox(checbox_frame, text="Вариант 2")
chekbox_2.grid(row=0, column=1)

window.mainloop()
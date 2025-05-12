from tkinter import *
from random  import randint

def random_color_and_place():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = f"#{r:02x}{g:02x}{b:02x}"

    window_width = 700
    window_height = 500

    button.update_idletasks()
    btn_width = button.winfo_width()
    btn_height = button.winfo_height()

    max_x = max(0, window_width - btn_width)
    max_y = max(0, window_height - btn_height)

    new_x = randint(0, max_x)
    new_y = randint(0, max_y)

    button.config(bg=color)
    button.place(x=new_x, y=new_y)

window = Tk()
window.title("Random button")
window.geometry("700x500")

button = Button(text="Нажми меня", font=("Arial", 10), command=random_color_and_place, width=15, height=2)
button.place(x=300, y=200)

window.mainloop()
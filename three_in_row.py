from tkinter import *
window = Tk()
for c in range(3): window.columnconfigure(index=c, weight=1)
for r in range(1): window.columnconfigure(index=r, weight=1) # columnconfigure

btn_1 = Button(window, text="Кнопка 1", font=("Arial", 15)) # window
btn_1.grid(row=0, column=0) # row

btn_2 = Button(window, text="Кнопка 2", font=("Arial", 15))
btn_2.grid(row=0, column=1) # column

btn_3 = Button(window, text="Кнопка 3", font=("Arial", 15))
btn_3.grid(row=0, column=2) # 0 2

window.mainloop()
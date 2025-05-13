from tkinter import *
window =Tk()
window.geometry("350x300")

for c in range(2): window.columnconfigure(index=c, weight=1)
for r in range(2):window.rowconfigure(index=r, weight=1)

button_1 = Button(window,text="Кнопка 1", font=("Arial", 11))
button_1.grid(row=0, column=0)

button_2 = Button(window,text="Кнопка 2", font=("Arial", 11),height=10)
button_2.grid(row=0, column=1, rowspan=2)

button_3 = Button(window,text="Кнопка 3", font=("Arial", 11))
button_3.grid(row=1, column=0, columnspan=1)

window.mainloop()
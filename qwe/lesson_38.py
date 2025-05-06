from tkinter import *

window = Tk()
window.title("Анкета")
window.geometry("700x500")

def check():
    print(name.get(), selected.get(), age.get(), chek_state.get())
    # laber_1.configure(text=f"Спасибо, {name.get()}")
    laber_1["text"] = f"Спасибо, {name.get()}"

laber_1 = Label(text="Расскажите о себе", font=("Arial", 20))
laber_1.place(x=220, y=10)

about = Message(text="Мы рады приветствовать вас на нашей анкете дружбы! Пожалуйста, отвечайте на вопросы честно, вся информация останется между нами.", font=("Arial", 14), width=680)
about.configure(justify=CENTER)
about.place(x=5, y=70)

name = Entry(width=50)
name.place(x=70, y=155)

laber_name = Label(text="ФИО:",font=("Arial", 15))
laber_name.place(x=5, y=150)

selected = IntVar()
rad_1 = Radiobutton(text="Мужской", font=("Arial", 10), value=1, variable=selected)
rad_2 = Radiobutton(text="Женский", font=("Arial", 10), value=2, variable=selected)
rad_1.place(x=10, y=200)
rad_2.place(x=100, y=200)

laber_age = Label(text="Сколько вам лет?", font=("Arial", 15))
laber_age.place(x=5, y=250)

age = Spinbox(from_=5, to=100, width=20)
age.place(x=10, y=300)

chek_state = IntVar()
chek_bnt_1 = Checkbutton(text="Запомнить меня", variable=chek_state)
chek_bnt_2 = Checkbutton(text="Не запоминать меня", variable=chek_state)
chek_bnt_3 = Checkbutton(text="Я останусь", variable=chek_state)
chek_bnt_1.place(x=10, y=350)
chek_bnt_2.place(x=150, y=350)
chek_bnt_3.place(x=300, y=350)

btn = Button(text="Отправить", font=("Arial", 10), background="green", fg="white", command=check)
btn.place(x=10, y=400)

window.mainloop()
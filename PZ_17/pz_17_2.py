#Даны три целых числа. Найти среднее из них (то есть число, расположенное между наименьшим и наибольшим).
from tkinter import *


def find_aver(event):
    try:
        a = int(num1.get())
        b = int(num2.get())
        c = int(num3.get())
        if (a >= b >= c) or (a <= b <= c):
            t = b
        elif (b >= a >= c) or (b <= a <= c):
            t = a
        else:
            t = c
        result['text'] = f"Среднее число: {t}"
    except ValueError:
        result['text'] = "Ошибка: введите числа!"

root = Tk()
root.title("Поиск среднего числа")
root.geometry("300x200+200+200")

Label(text="Первое число:").grid(row=1, column=0)
num1 = Entry()
num1.grid(row=1, column=1)

Label(text="Второе число:").grid(row=2, column=0)
num2 = Entry()
num2.grid(row=2, column=1)

Label(text="Третье число:").grid(row=3, column=0)
num3 = Entry()
num3.grid(row=3, column=1)

calculate = Button(text="Найти среднее")
calculate.grid(row=4, column=0, columnspan=2, pady=10)

result = Label()
result.grid(row=5, column=0, columnspan=2)

calculate.bind('<Button-1>', find_aver)

root.mainloop()
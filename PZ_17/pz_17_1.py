# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Testform')
root.geometry('650x450')

padx = 10 # гор отступ
pady = 5

Label(root, text='Name:').grid(row=0, column=0, sticky='w', padx=padx, pady=pady)
name_entry = Entry(root, width=25)
name_entry.grid(row=0, column=1, sticky='w', padx=padx, pady=pady)


Label(root, text='Password:').grid(row=1, column=0, sticky='w', padx=padx, pady=pady)
password_entry = Entry(root, show='*', width=25)
password_entry.grid(row=1, column=1, sticky='w', padx=padx, pady=pady)


Label(root, text='Gender:').grid(row=2, column=0, sticky='nw', padx=padx, pady=pady)
gender_frame = Frame(root)
gender_frame.grid(row=2, column=1, sticky='w')

var = IntVar()
var.set(0)
Radiobutton(gender_frame, text='Male', variable=var, value=0).pack(anchor='w')
Radiobutton(gender_frame, text='Female', variable=var, value=1).pack(anchor='w')


Label(root, text='Continent:').grid(row=3, column=0, sticky='w', padx=padx, pady=pady)
options = ["Africa", "Asia", "Europe", "North America", "South America", "Australia", "Antarctica"]
combo = ttk.Combobox(root, values=options, state='readonly', width=22)
combo.set("Please select...")
combo.grid(row=3, column=1, sticky='w', padx=padx, pady=pady)


Label(root, text='Meals:').grid(row=4, column=0, sticky='nw', padx=padx, pady=pady)
meals_frame = Frame(root)
meals_frame.grid(row=4, column=1, sticky='w')

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
Checkbutton(meals_frame, text='breakfast', variable=var1, onvalue=1, offvalue=0).pack(anchor='w')
Checkbutton(meals_frame, text='lunch', variable=var2, onvalue=1, offvalue=0).pack(anchor='w')
Checkbutton(meals_frame, text='dinner', variable=var3, onvalue=1, offvalue=0).pack(anchor='w')


Label(root, text='Remark:').grid(row=5, column=0, sticky='nw', padx=padx, pady=pady)
text1 = Text(root, height=4, width=25, wrap=WORD)
text1.grid(row=5, column=1, sticky='w', padx=padx, pady=pady)


buttons_frame = Frame(root)
buttons_frame.grid(row=6, column=2, sticky='e', pady=15)

Button(buttons_frame, text='Cancel', width=10).pack(side=LEFT, padx=5)
Button(buttons_frame, text='Submit', width=10).pack(side=LEFT, padx=5)

root.mainloop()
#класс tk
import tkinter as tk

#создание объкта класса tk, то есть окно
win = tk.Tk()
#название
win.title('Крестики-нолики')

#длина и ширина и расположение
win.geometry('400x300+500+200')

#разрешение на изменение окна
win.resizable(True, False)

#максимальные и минимальные значения размеров окна
win.minsize(300, 150)
win.maxsize(600, 450)

#создадим объект класса фото-имейдж из библиотке tk, а после загружаем в объект win
photo = tk.PhotoImage(file='tic-tac-toe.png')
win.iconphoto(False, photo)

#цвет фона
win.config(bg='#FFC0CB')

'''
#первый лайбл
label_1 = tk.Label(win, text = 'Hello!',
                   bg='#DB7093',#цвет фона текста
                   fg='#A9A9A9',#цвет текста
                   font=('TkMenuFont', 15, 'normal'),#шрифт, то есть шрифт, размер, статус(жир, норм)
                   width=5,#ширина
                   height=5,#высота
                   #padx=10,#расположение по оси х в зоне от стен
                   #pady=10,#расположение по оси y в зоне от стен
                   anchor='center',#расположние в зоне в цетнре
                   relief=tk.RAISED,#рельеф, как у кнопки
                   bd=10,#типа насколько заметна эта кнопка
                   justify=tk.RIGHT#по какой стороне будет выравниваться текст
                   )
#вызов первого лайбл
label_1.pack()
'''

'''
#бета-функции
def print_X():
    label_X = tk.Label(win, text='X')
    label_X.pack()

def print_O():
    label_O = tk.Label(win, text='O')
    label_O.pack()

def print_count():
    global count
    count+=1
    button_4['text'] = f'Count: {count}'

#переменная для print_count
count = 0

#обратимся к классу баттон из библиотеки и создадим кнопки
button_1 = tk.Button(win, text='X',
                     command=print_X    #вызов функции
                     )
button_1.pack()

button_2 = tk.Button(win, text='O',
                     command=print_O    #вызов функции
                     )
button_2.pack()

button_3 = tk.Button(win, text='Game',
                     command= lambda: tk.Label(win, text='Game').pack()   #вызов ляьда-функции без def
                     )
button_3.pack()

button_4 = tk.Button(win, text=f'Count: {count}',
                    command=print_count,
                    activebackground='blue',    #при нажатии менят цвет
                    bg='red'
                    )
button_4.pack()
'''

'''
button_0_1 = tk.Button(win, text='X')
button_0_2 = tk.Button(win, text='O')
button_0_3 = tk.Button(win, text='Game')

#расположение кнопок по grid типа матрицы
button_0_1.grid(row=0, column=0)
button_0_2.grid(row=0, column=1)
button_0_3.grid(row=1, column=0, columnspan=2, stick='we')#типа заполнит лево и право
'''

"""def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('not Entry')

def delete_entry():
    name.delete(0)


label_1_0 = tk.Label(win, text='имя: ', bg='pink').grid(row=0, column=0, stick='w')
name = tk.Entry(win)
name.grid(row=0, column=1)
tk.Button(win, text='get', command=get_entry).grid(row=1, column=0, stick='we')
tk.Button(win, text='delete', command=delete_entry).grid(row=1, column=1, stick='we')
tk.Button(win, text='insert', command=lambda: name.insert(0, 'YES')).grid(row=2, column=0, columnspan=2, stick='we')


win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)
"""


#показать окно
win.mainloop()

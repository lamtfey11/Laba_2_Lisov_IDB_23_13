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

#показать окно
win.mainloop()

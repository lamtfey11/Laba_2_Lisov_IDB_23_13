#класс tk
import tkinter as tk

#создание объкта класса tk
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

#показать окно
win.mainloop()

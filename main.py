from tkinter import *


game = [None] * 9
game_left = list(range(9))
turn = 0

root = Tk()
label = Label(width=20, text = 'Крестики-нолики')

#длина и ширина и расположение
root.geometry('400x300+500+200')
#разрешение на изменение окна
root.resizable(True, False)
#максимальные и минимальные значения размеров окна
root.minsize(300, 150)
root.maxsize(600, 450)

root.mainloop()
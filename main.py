from tkinter import *

#длина и ширина и расположение
#root.geometry('400x300+500+200')
#разрешение на изменение окна
#root.resizable(True, False)
#максимальные и минимальные значения размеров окна
#root.minsize(300, 150)
#root.maxsize(600, 450)

def win_check(game, turn):
    if game[0] == game[1] == game[]
    return 0

def puch(x):
    global game, turn
    if win_check(game, turn) == 0:
        if turn % 2 == 0:
            game[x] == 'X'
            button[x].config(text = 'X', bg = 'white', state = 'disabled')
            turn += 1
        elif turn % 2 != 0:
            game[x] == 'O'
            button[x].config(text = 'O', bg = 'white', state = 'disabled')
            turn += 1
        

        

game = [None] * 9
turn = 0


root = Tk()
label = Label(width=20, text = 'Крестики-нолики')
button = [Button(width=4, height=2, font=('Arial', 25, 'bold'), bg="pink", command=lambda x=i: puch(x)) for i in range(9)]
label.grid(row=0, column=0, columnspan=3)



row = 1
col = 0

for i in range(9):
    button[i].grid(row=row, column=col)
    col += 1    
    if col == 3:
        row += 1
        col = 0



root.mainloop()
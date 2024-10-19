from tkinter import *


def win_check(x):
    global game
    global turn
    if game[x] == 'X' and ((game[6]  == game[x] and game[7]  == game[x] and game[8]  == game[x]) or (game[3]  == game[x] and game[4]  == game[x] and game[5]  == game[x]) or (game[0]  == game[x] and game[1]  == game[x] and game[2]  == game[x]) or (game[0]  == game[x] and game[3]  == game[x] and game[6]  == game[x]) or (game[1]  == game[x] and game[4]  == game[x] and game[7]  == game[x]) or (game[8]  == game[x] and game[5]  == game[x] and game[2]  == game[x]) or (game[2]  == game[x] and game[4]  == game[x] and game[6]  == game[x]) or (game[0]  == game[x] and game[4]  == game[x] and game[8]  == game[x])):
        return 1
    elif game[x] == 'O' and ((game[6]  == game[x] and game[7]  == game[x] and game[8]  == game[x]) or (game[3]  == game[x] and game[4]  == game[x] and game[5]  == game[x]) or (game[0]  == game[x] and game[1]  == game[x] and game[2]  == game[x]) or (game[0]  == game[x] and game[3]  == game[x] and game[6]  == game[x]) or (game[1]  == game[x] and game[4]  == game[x] and game[7]  == game[x]) or (game[8]  == game[x] and game[5]  == game[x] and game[2]  == game[x]) or (game[2]  == game[x] and game[4]  == game[x] and game[6]  == game[x]) or (game[0]  == game[x] and game[4]  == game[x] and game[8]  == game[x])):
        return 2
    elif turn == 9:
        return 3
    else:
        return 0


def puch(x):
    global game, turn
    if turn % 2 == 0:
        game[x] = 'X'
        button[x].config(text = 'X', state = 'disabled')
        turn += 1
    elif turn % 2 != 0:
        game[x] = 'O'
        button[x].config(text = 'O', state = 'disabled')
        turn += 1

    if win_check(x) == 1:
        label['text'] = 'Победа Х'
        for i in range(9):
            button[i].config(state='disabled')
    elif win_check(x) == 2:
        label['text'] = 'Победа О'
        for i in range(9):
            button[i].config(state='disabled')
    elif win_check(x) == 3:
        label['text'] = 'Ничья'
        for i in range(9):
            button[i].config(state='disabled')

def newGame():
    global game
    global turn 
    game = [None] * 9
    turn = 0
    row = 1
    col = 0
    for i in range(9):
        if i == 0:
            button[i].config(text = '', bg = 'white', state = 'active')
        elif i == 1:
            button[i].config(text = '', bg = 'white', state = 'active')
        elif i == 2:
            button[i].config(text = '', bg = 'white', state = 'active')
        elif i == 3:
            button[i].config(text = '', bg = 'white', state = 'active')
        elif i == 4:
            button[i].config(text = '', bg = 'white', state = 'active')
        elif i == 5:
            button[i].config(text = '', bg = 'white', state = 'active')
        elif i == 6:
            button[i].config(text = '', bg = 'white', state = 'active')
        elif i == 7:
            button[i].config(text = '', bg = 'white', state = 'active')
        elif i == 8:
            button[i].config(text = '', bg = 'white', state = 'active')
        col += 1    
        if col == 3:
            row += 1
            col = 0
def Exit():
    root.quit()      

game = [None] * 9
turn = 0


root = Tk()
#длина и ширина и расположение
root.geometry('270x340+500+200')
#разрешение на изменение окна
root.resizable(True, True)
#максимальные и минимальные значения размеров окна
#root.minsize(300, 150)
root.maxsize(600, 450)

label = Label(width=20, text = 'Крестики-нолики')
button = [Button(width=4, height=2, font=('Arial', 25, 'bold'), bg="white", command=lambda x=i: puch(x)) for i in range(9)]
label.grid(row=0, column=0, columnspan=3)



row = 1
col = 0

# Настройка веса столбцов
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 3, weight=1)
for i in range(9):
    if i == 0:
        button[i].grid(row=row, column=col, sticky="NSEW")
    elif i == 1:
        button[i].grid(row=row, column=col, sticky="NSEW")
    elif i == 2:
        button[i].grid(row=row, column=col, sticky="NSEW")
    elif i == 3:
        button[i].grid(row=row, column=col, sticky="NSEW")
    elif i == 4:
        button[i].grid(row=row, column=col, sticky="NSEW")
    elif i == 5:
        button[i].grid(row=row, column=col, sticky="NSEW")
    elif i == 6:
        button[i].grid(row=row, column=col, sticky="NSEW")
    elif i == 7:
        button[i].grid(row=row, column=col, sticky="NSEW")
    elif i == 8:
        button[i].grid(row=row, column=col, sticky="NSEW")
    col += 1    
    if col == 3:
        row += 1
        col = 0
     
#убирает пунктир
root.option_add("*tearOff", False)

#Game
main_menu = Menu()#под Game
Game_menu = Menu()

Game_menu.add_command(label="Exit", command=Exit)
Game_menu.add_command(label="New Game", command=newGame)
#сама надпись Game
main_menu.add_cascade(label="Game", menu=Game_menu)
root.config(menu=main_menu)

root.mainloop()
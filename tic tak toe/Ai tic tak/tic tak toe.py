from tkinter import *
from tkinter import messagebox




def click(row, column):

    global playerturn
    if board[row][column] == ' ':
        if playerturn:
            board[row][column] = 'X'
            buttons[row][column].config(text='X')
            if checkForWinner('X'):
                messagebox.showinfo("game Over", "player wins!")

                resetGame()
            elif checkForDraw(board):
                messagebox.showinfo("game Over", "its a draw!")

                resetGame()
            else:
                playerturn = False
                ai_move()

def ai_move():
    global playerturn
    best_score = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    board[best_move[0]][best_move[1]] = 'O'
    buttons[best_move[0]][best_move[1]].config(text='O')

    if checkForWinner('O'):

        messagebox.showinfo("Game Over", "AI wins!")
        resetGame()

    elif checkForDraw(board):
        messagebox.showinfo("Game Over", "It's a draw!")
        resetGame()

    else:
        playerturn = True

def minimax(board, depth, is_maximizing):

    if checkForWinner('X'):
        return -10 + depth
    elif checkForWinner('O'):
        return 10 - depth
    
    elif checkForDraw(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '

                    best_score = max(score, best_score)


        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':

                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score
    



def checkForWinner(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:

        return True
    return False

def checkForDraw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def resetGame():
    global board, playerturn
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for row in buttons:
        for button in row:
            button.config(text='')
    playerturn = True

root = Tk()
root.title("Tic-Tac-Toe with AI")
root.geometry("500x400+200+100")
root.config(bg="lightblue")


##icon image
icon_image=PhotoImage(file="unnamed.png")
root.iconphoto(False,icon_image)

Label(root,text="TIC",font="Arial 30 bold",bg="lightblue",fg="white").place(x=400,y=100)
Label(root,text="TAC",font="Arial 30 bold",bg="lightblue",fg="white").place(x=400,y=150)
Label(root,text="TOE",font="Arial 30 bold",bg="lightblue",fg="white").place(x=400,y=200)

playerturn = True
buttons = []
board = [[' ' for _ in range(3)] for _ in range(3)]

for i in range(3):
    row = []
    for j in range(3):
        button = Button(root, command=lambda row=i, column=j: click(row, column), bg="white",fg="red",height=3,bd=1,cursor="hand1",width=6, font=("Arial", 24))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

root.mainloop()

board = [
    ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' '
]


def horizontalwinner():
    if board[1] == 'X' and board[2] == 'X' and board[3] == 'X':
        printboard(board)
        print("X Won")
        exit()
    elif board[4] == 'X' and board[5] == 'X' and board[6] == 'X':
        printboard(board)
        print("X Won")
        exit()
    elif board[7] == 'X' and board[8] == 'X' and board[9] == 'X':
        printboard(board)
        print("X Won")
        exit()
    elif board[1] == 'O' and board[2] == 'O' and board[3] == 'O':
        printboard(board)
        print("O Won")
        exit()
    elif board[4] == 'O' and board[5] == 'O' and board[6] == 'O':
        printboard(board)
        print("O Won")
        exit()
    elif board[7] == 'O' and board[8] == 'O' and board[9] == 'O':
        printboard(board)
        print("O Won")
        exit()
    else:
        pass


def verticalwinner():
    if board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        printboard(board)
        print("X Won")
        exit()
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        printboard(board)
        print("X Won")
        exit()
    elif board[3] == 'X' and board[6] == 'X' and board[9] == 'X':
        printboard(board)
        print("X Won")
        exit()
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        printboard(board)
        print("O Won")
        exit()
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        printboard(board)
        print("O Won")
        exit()
    elif board[3] == 'O' and board[6] == 'O' and board[9] == 'O':
        printboard(board)
        print("O Won")
        exit()
    else:
        pass


def diagonalwinner():
    if board[1] == 'X' and board[5] == 'X' and board[9] == 'X':
        printboard(board)
        print("X Won")
        exit()
    elif board[3] == 'X' and board[5] == 'X' and board[7] == 'X':
        printboard(board)
        print("X Won")
        exit()
    elif board[1] == 'O' and board[5] == 'O' and board[9] == 'O':
        printboard(board)
        print("O Won")
        exit()
    elif board[3] == 'O' and board[5] == 'O' and board[7] == 'O':
        printboard(board)
        print("O Won")
        exit()
    else:
        pass


def smart():
    if plax == plao:
        print("Don't Worry I Am Smart")
    else:
        pass


def plx():
    global plax
    try:
        plax = int(input("X Enter The Number[1,9] Here: "))
        if board[plax] == 'O':
            print("Don,t Worry I Am Smart")
            printboard(board)
            plx()
        elif board[plax] == 'X':
            print("Don,t Worry I Am Smart")
            printboard(board)
            plx()
        else:
            pass
    except Exception as t:
        print(t)
        plx()
    board[plax] = 'X'
    horizontalwinner()
    diagonalwinner()
    verticalwinner()
    checkboard()
    return 0

def plo():
    global plao
    try:
        plao = int(input("O Enter The Number[1,9] Here: "))
        if board[plao] == 'X':
            print("Don,t Worry I Am Smart")
            printboard(board)
            plo()
        elif board[plao] == 'O':
            print("Don,t Worry I Am Smart")
            printboard(board)
            plx()
        else:
            pass
    except Exception as e:
        print(e)
        plo()
    board[plao] = 'O'
    horizontalwinner()
    diagonalwinner()
    verticalwinner()
    checkboard()
    return 0


def checkboard():
    if board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[
        5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9]:
        printboard(board)
        print("Board is Full No One Won")
        exit()
    else:
        pass


def printboard(board):
    print(f'{board[1]}|{board[2]}|{board[3]}')
    print(f'-+-+-')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print(f'-+-+-')
    print(f'{board[7]}|{board[8]}|{board[9]}')


if __name__ == '__main__':
    printboard(board)
    while True:
        plx()
        printboard(board)
        plo()
        printboard(board)

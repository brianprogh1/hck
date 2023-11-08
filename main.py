from db import Database
from colorama import Fore, Style, Back

bg_color = Back.GREEN
sr = Style.RESET_ALL
dbs = Database()


def sum(a, b, c):
    return a + b + c


def leaderboard():
    print(' LEADERBOARD '.center(52, "-"))
    table = dbs.lead()
    print('|' + 'Name'.center(30) + '|' + 'Wins'.center(20) + '|')
    for col in table:
        print('-' * 53)
        print('|' + f'{col[0]}'.center(30) + '|' + f'{col[1]}'.center(20) + '|')
    print('-' * 53)


def printBoard(xState, zState):
    for i in range(1, 10):
        symbol = Fore.RED + 'X' + Style.RESET_ALL if xState[i] else (Fore.BLUE + 'O' + Style.RESET_ALL if zState[i] else str(i))
        print(bg_color + symbol + sr, end=Fore.BLACK+bg_color+' | '+sr if i % 3 != 0 else '\n')
        if i % 3 == 0 and i != 9:
            print(Fore.BLACK+bg_color+"--|---|--"+sr)


def checkWin(xState, zState):
    global p1, p2
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X Won the match")
            prev = dbs.query(p1)
            if not prev:
                dbs.add(p1, 1)
            else:
                dbs.add(p1, prev[0] + 1)
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O Won the match")
            prev = dbs.query(p2)
            if not prev:
                dbs.add(p2, 1)
            else:
                dbs.add(p2, prev[0] + 1)
            return 0
    return -1


leaderboard()
if __name__ == "__main__":
    p1 = input(Fore.GREEN+"Enter name of Player 1: "+Style.RESET_ALL)
    p2 = input(Fore.GREEN+"Enter name of Player 2: "+Style.RESET_ALL)
    xState = [0] * 10
    zState = [0] * 10
    turn = 1
    count = 0
    print("Welcome to Tic Tac Toe")
    while True:
        printBoard(xState, zState)
        if count >= 9:
            print("It's a draw")
            break
        if turn == 1:
            print(f"{Fore.RED}X's Chance ({p1}){Style.RESET_ALL}")
        else:
            print(f"{Fore.BLUE}O's Chance ({p2}){Style.RESET_ALL}")
        value = int(input("Please enter a value (1-9): "))
        if xState[value] == 0 and zState[value] == 0:
            if turn == 1:
                xState[value] = 1
            else:
                zState[value] = 1
            count += 1
        else:
            print("Invalid move. Cell is already occupied. Try again.")
            continue

        cwin = checkWin(xState, zState)
        if cwin != -1:
            printBoard(xState, zState)
            print(Fore.MAGENTA+"\nMatch over\n"+sr)
            break

        turn = 1 - turn
leaderboard()


ch = input('Do you want to reset Leaderboard? [y/n]: ')
if ch.lower() == 'y':
    dbs.reset()

dbs.exit()

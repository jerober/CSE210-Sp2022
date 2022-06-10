# W01: Tic-Tac-Toe Game Jessica Robertson

from re import I


theBoard = {
            '7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' 
}

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def main():

    turn = 'X'
    count = 0
    player1 = 'Player 1'
    player2 = 'Chocolate Thunder'
    player = player1

    print("It's " + player1 + "'s turn")

    while count < 10:
        printBoard(theBoard)

        move = input()

        # This runs each turn
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print('That spot is already filled. \nPlease choose another.')
            continue

        #Possible winning statements
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(player + " won.")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(player + " won.")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(player + " won.")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(player + " won.")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(player + " won.")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(player + " won.")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(player + " won.")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(player + " won.")
                break 

        if count == 9:
            print("\nGame Over.\n")
            print("Cat Game (what does that even mean??)")

        # The turn switches from an 'X' to an 'O' every turn
        if turn == 'X':
            player = player2
            print("It's " + player + "'s turn")
            turn = 'O'

        else: 
            player = player1
            print("It's " + player + "'s turn")
            turn = 'X'

main()
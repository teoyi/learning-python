# Python - Tic Tac Toe Project
'''A simple TIC-TAC-TOE project to signify my first milestone in learning the python language'''

def title():
    # WELCOME MESSAGE
    print('\n\t   Welcome to the TIC-TAC-TOE Project!')

    # Instructions
    print('''
    ______________________________________________________
    INSTRUCTIONS:

    The board consists of 9 squares for you to fill:

                |   7   |   8   |   9   |
                |-------+-------+-------|
                |   4   |   5   |   6   |
                |-------+-------+-------|
                |   1   |   2   |   3   |

    When requested for your input, select a value from 1
    to 9 and either an X or an O (depending on the turn)
    will appear to take the spot desired.

    If you would like to exit the project at any point of
    time, please input 0.

    NOTE: Player 1 - X
          Player 2 - O

          Player 1 = X, will always start first!!''')



# DICTIONARY TO STORE PLAYER INPUT
theboard = {'7':' ', '8':' ', '9':' ',
            '4':' ', '5':' ', '6':' ',
            '1':' ', '2':' ', '3':' '}


# CREATING DISPLAY BOARD W/ DICTIONARY
def display_board(board):
    print('\nThe current board is:\n ')
    row1 = [board['7'],'|',board['8'],'|',board['9']]
    row2 = ['-','-','-','-','-']
    row3 = [board['4'],'|',board['5'],'|',board['6']]
    row4 = ['-','-','-','-','-']
    row5 = [board['1'],'|',board['2'],'|',board['3']]

    print(''.join(row1))
    print(''.join(row2))
    print(''.join(row3))
    print(''.join(row4))
    print(''.join(row5))


# CODE FOR THE GAME
def game():
    turn = 'X'
    count = 0

    # ASK/CHECK INPUT
    for i in range(10):
        display_board(theboard)

        # CHECKING INPUT
        move = 'WRONG'
        acceptable_range = range(0,10)
        within_range = False
        while move.isdigit() == False or within_range == False:

            # CHECKING DIGIT
            move =  str(input('\nWhere would you like to place %s? (1-9) : ' % turn))
            if move.isdigit() == False:
                print('Sorry, that is not an appropriate value!')

            # CHECKING IF IT IS WITHIN range
            if move.isdigit() == True:
                if int(move) in acceptable_range:
                    within_range = True
                    continue
                else:
                    print('Sorry, that is not within the range provided! (1 - 9)')

        if move == '0':
            print('______________________________________________________')
            print('Thank you for playing! Have a good day!\n')
            print('Closing project...')
            exit()
        if theboard[move] == ' ':
            theboard[move] = turn
            count += 1
            print('\nTURN ' + str(count))
        else:
            print('This position is already filled, please choose another!')
            continue

        # POSSIBLE OUTCOMES UPON REACHING COUNT >= 5

        if count >= 5:

            # CHECKING VERTICAL WIN
            if theboard['7'] == theboard['4'] == theboard['1'] != ' ':
                display_board(theboard)
                print('\nGame Over!')
                print(turn + ' wins!')
                break

            elif theboard['8'] == theboard['5'] == theboard['2'] != ' ':
                display_board(theboard)
                print('\nGame Over!')
                print(turn + ' wins!')
                break

            elif theboard['9'] == theboard['6'] == theboard['3'] != ' ':
                display_board(theboard)
                print('\nGame Over!')
                print(turn + ' wins!')
                break

            # CHECKING HORIZONTAL WIN
            elif theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                display_board(theboard)
                print('\nGame Over!')
                print(turn + ' wins!')
                break

            elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                display_board(theboard)
                print('\nGame Over!')
                print(turn + ' wins!')
                break

            elif theboard['1'] == theboard['2'] == theboard['3'] != ' ':
                display_board(theboard)
                print('\nGame Over!')
                print(turn + ' wins!')
                break

            # CHECKING DIAGONAL WIN
            elif theboard['7'] == theboard['5'] == theboard['3'] != ' ':
                display_board(theboard)
                print('\nGame Over!')
                print(turn + ' wins!')
                break
            elif theboard['9'] == theboard['5'] == theboard['1'] != ' ':
                display_board(theboard)
                print('\nGame Over!')
                print(turn + ' wins!')
                break

            # DRAW
            if count == 9:
                print('\nIt\'s a draw! Better luck next time!')
                break

        # Turn switches over to the other person after a move
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


    # CONTINUE STATEMENT
    restart = 'chicken'

    while restart != 'y' or restart != 'n':

        restart = input('\nWould you like to continue? (Y/N) :  ')
        if restart.lower() == 'y':
            for n in theboard:
                theboard[n] = ' '
            game()
        elif restart.lower() == 'n':
            print('______________________________________________________')
            print('Thank you for playing! Have a good day!\n')
            print('Closing Tic-Tac-Toe Project...')
            print('\n')
            exit()
        else:
            print('Invalid Command, Please Try Again.')
            continue


title()
game()

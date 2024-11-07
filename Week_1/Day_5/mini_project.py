import itertools

in_game = True
players = ['X', '0']
iter_players = itertools.cycle(players)
board = [
    ['   ','   ','   '],
    ['   ','   ','   '],
    ['   ','   ','   ']
]
win_combinations = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)]
]

print("\nWelcome to TIC TAC TOE")

def display_board():
    print("\nTIC TAC TOE")
    print("*******************")
    for index, row in enumerate(board):
        row_w_div = (" | ".join(row))
        print(f'* {row_w_div} *')

        if index < len(board) - 1:
            print('* --- | --- | --- *')

    print("*******************\n")

display_board()

def check_win(row,col,player):
    player_input = board[row][col]
    combo_matches = 0

    print('check_win')
    for combo in win_combinations:
        for cell in combo:
            # print("Board cell... " + board[cell[0]][cell[1]])
            # print("Player input " + player_input)
            # if (board[cell[0]][cell[1]] != '   ') and (board[cell[0]][cell[1]] == player_input):
            if (board[cell[0]][cell[1]] != '   '):
                combo_matches += 1
                print("combo", combo_matches)
                print(f'Combo matches = {combo_matches}')

        if combo_matches == 3:
            in_game = False

def play():
    current_player = next(iter_players)


    print(f'Player {current_player}\'s turn.\n')

    row = (int(input('Enter row: ')))-1
    col = (int(input('Enter column: ')))-1

    board[row][col] = f' {current_player} '

    display_board()

    check_win(row,col,current_player)

while in_game == True:
    play()
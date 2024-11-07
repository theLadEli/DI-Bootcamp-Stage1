import itertools

in_game = True
players = ['X', 'Y']
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

def play():
    current_player = next(iter_players, )

    display_board()
    print(f'Player {current_player}\'s turn.\n')

    row = (int(input('Enter row: ')))-1
    col = (int(input('Enter column: ')))-1

    board[row][col] = f' {current_player} '

    display_board()

    check_win(row,col,current_player)

def check_win(row,col,player):
    combo_matches = 0

    for combo in win_combinations:
        for cell in combo:
            for value in cell:
                if value == (row,col):
                    combo_matches += 1
                    print(f'Combo matches = {combo_matches}')

        if combo_matches == 3:
            in_game = False

while in_game == True:
    play()
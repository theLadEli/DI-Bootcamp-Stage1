print("Welcome to TIC TAC TOE")

board = [
    [' ',' ',' ']
    [' ',' ',' ']
    [' ',' ',' ']
]

def display_board():
    for row in board:
        for cell in row:
            print(f'{item} | ')
        print("-------------")

display_board()

# print("TIC TAC TOE")
# print("****************")
# print("")
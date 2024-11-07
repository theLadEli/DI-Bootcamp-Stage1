board = [
    [" ", " ", " "], 
    [" ", " ", " "],  
    [" ", " ", " "]  
]
#function that displays the board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def check_winner(board, player):
    #this checks rows and columns
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

#check if the board is full tie 
def check_tie(board):
    return all(cell != " " for row in board for cell in row)

#main function for the game itself
def tictac():
    board = [[" " for _ in range(3)] for _ in range(3)] 
    current_player = "X"
    game_over = False

    while not game_over:
        display_board(board)
        print(f"Player {current_player}'s turn")

        while True:
            try:
                row = int(input("Enter the row (0, 1, 2): "))
                col = int(input("Enter the column (0, 1, 2): "))
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter numbers between 0 and 2 for row and column.")

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tictac()
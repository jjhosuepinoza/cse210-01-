''' TIC-TAC-TOE GAME
    Author: Javier Espinoza
'''

def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player,board)
        player = next_player(player)
    display_board(board)
    print("That was a good game!")

def create_board():
    board = []
    for square in range (9):
        board.append(square +1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def is_a_draw(board):
    for square in range(9):
        if board[square]!="X" and board[square] !="O":
            return False
    return True
"""
Algorithm

Starting with an incomplete board:
    - Find some empty space
    - Attempt to place the digits 1-9 in that space
    - Check if that digit is valid in the current spot based on the current board
      - If the digit is valid, recursively attempt to fill the board using steps 1-3.
      - If it is not valid, reset the square you just filled and go back to the previous step.
    - Once the board is full by the definition of this algorithm we have found a solution.
"""

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    
    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False


def valid(board, num, pos):
    # Check row
    for row in range(len(board[0])):
        if board[pos[0]][row] == num and pos[1] != row:
            return False

    # Check column
    for col in range(len(board)):
        if board[col][pos[1]] == num and pos[0] != col:
            return False

    # Check box
    box_y = pos[0] // 3
    box_x = pos[1] // 3
    for row in range(box_y*3, box_y*3 + 3):
        for col in range(box_x*3, box_x*3 + 3):
            if board[row][col] == num and (row, col) != pos:
                return False
    
    return True

            

def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("-----------------------")
        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")


def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)
    
    return None


if __name__ == '__main__':
    print("\n --- Sodoku Problem ---\n")
    print_board(board)
    solve(board)
    print("\n --- Solution Board ---\n")
    print_board(board)
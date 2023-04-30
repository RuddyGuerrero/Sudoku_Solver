def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

    return None


def is_valid(board, pos, num):
    for i in range(9):
        if board[pos[0]][i] == num:
            return False

    for i in range(9):
        if board[i][pos[1]] == num:
            return False

    x = (pos[0]) // 3
    y = (pos[1]) // 3
    for i in range(x * 3, (x + 1) * 3):
        for j in range(y * 3, (y + 1) * 3):
            if board[i][j] == num:
                return False

    return True


def solve(board):

    empty = find_empty(board)
    if not empty:
        return True

    for num in range(1, 10):

        if is_valid(board, empty, num):
            board[empty[0]][empty[1]] = num

            if solve(board):
                return True

            board[empty[0]][empty[1]] = 0

    return False


if __name__ == "__main__":

    board = [
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3],
        [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
    ]

    solve(board)
    print_sudoku(board)

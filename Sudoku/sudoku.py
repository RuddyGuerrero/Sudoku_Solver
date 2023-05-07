def print_sudoku(board):
    """
    Imprime el tablero de sudoku en la consola.
    
    Entrada:
        board (list of list of int): una matriz de 9x9 que representa el tablero
        de sudoku.
    
    Salida:
        None
    """

    # Iterar a través de las filas del tablero
    for i in range(9):
        # Imprimir una línea horizontal cada 3 filas
        if i % 3 == 0 and i != 0:
            print("- " * 11)
        # Iterar a través de las columnas del tablero
        for j in range(9):
            # Imprimir una línea vertical cada 3 columnas
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            # Imprimir el valor en la celda actual
            print(board[i][j], end=" ")
        # Imprimir una línea nueva después de cada fila
        print()


def find_empty(board):
    """
    Encuentra la posición de la próxima celda vacía en el tablero de sudoku.
    
    Entrada:
        board (list of list of int): una matriz de 9x9 que representa el tablero
        de sudoku.
    
    Salida:
        tuple of int: una tupla que contiene las coordenadas de la próxima celda vacía 
        (fila, columna), o None si no hay celdas vacías.
    """

    # Iterar a través de todas las celdas del tablero
    for i in range(9):
        for j in range(9):
            # Si la celda actual está vacía, devolver su posición
            if board[i][j] == 0:
                return i, j
    # Si no hay celdas vacías, devolver None
    return None


def is_valid_move(board, pos, num):
    """
    Verifica si un número es válido en una posición determinada del tablero de sudoku.
    
    Entrada:
        board (list of list of int): una matriz de 9x9 que representa el tablero de
        sudoku.
        pos (tuple of int): una tupla que contiene las coordenadas de la posición en
        la que se desea colocar el número (fila, columna).
        num (int): el número que se desea colocar en la posición especificada.
   
    Salida:
        bool: True si el número es válido en la posición dada, False de lo contrario.
    """

    # Comprobar si el número ya está en la fila
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Comprobar si el número ya está en la columna
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # Comprobar si el número ya está en el cuadrante
    x = (pos[0]) // 3
    y = (pos[1]) // 3
    for i in range(x * 3, (x + 1) * 3):
        for j in range(y * 3, (y + 1) * 3):
            if i == pos[0] and j == pos[1]:
                continue
            if board[i][j] == num:
                return False
    # Si el número no está en la fila, columna o cuadrante, es válido
    return True

def is_valid_board(board):
    """
    Verifica si el tablero de Sudoku dado es válido.

    Entrada:
        board (list[list[int]]): El tablero de Sudoku.

    Salida:
        bool: True si el tablero es válido, False en caso contrario.
    """

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                pos = (i, j)
                if not is_valid_move(board, pos, board[i][j]):
                    return False
    return True


def solve(board):
    """
    Resuelve el tablero de sudoku mediante una implementación de backtracking.
    Busca una celda vacía en el tablero, y luego intenta colocar números en esa
    celda. Si encuentra un número que es válido, coloca el número en la celda y
    llama recursivamente a la función solve para resolver el resto del tablero.
    Si la llamada recursiva a solve devuelve un tablero resuelto, devuelve ese
    tablero. Si no encuentra un número válido, retrocede y prueba otro número.

    Entrada:
        board (list of list of int): una matriz de 9x9 que representa el tablero de
        sudoku.

    Salida:
        list of list of int or None: una matriz de 9x9 que representa el tablero
        resuelto, o None si el tablero no se puede resolver.
    """

    # Encontrar la siguiente celda vacía en el tablero
    empty = find_empty(board)
    # Si no hay celdas vacías, se ha resuelto el tablero
    if not empty:
        return board
    # Probar cada número del 1 al 9 en la celda vacía
    for num in range(1, 10):
        # Comprobar si el número es válido en la celda vacía
        if is_valid_move(board, empty, num):
            # Asignar el número a la celda vacía
            board[empty[0]][empty[1]] = num
            # Llamar recursivamente a solve() con el tablero actualizado
            if solve(board) is not None:
                return board
            # Si solve() devuelve None, volver a asignar 0 a la celda vacía
            board[empty[0]][empty[1]] = 0
    # Si ningún número del 1 al 9 es válido en la celda vacía, devolver None
    return None


if __name__ == "__main__":

    # Ejemplo de tablero de Sudoku para resolver
    board = [
        [6, 0, 8, 4, 1, 9, 7, 0, 5],
        [0, 0, 0, 0, 2, 0, 1, 0, 3],
        [2, 1, 7, 3, 0, 8, 9, 0, 6],
        [8, 0, 3, 0, 0, 0, 2, 9, 0],
        [0, 5, 1, 9, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 4, 0, 8, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 8, 0, 5, 6, 0, 0],
        [0, 8, 2, 0, 6, 4, 0, 0, 0],
    ]

    # print_sudoku(solve(board))

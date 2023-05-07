import sys

from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Sudoku import solve
from Sudoku import is_valid_move
from Sudoku import is_valid_board


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Se carga la interfaz gráfica desde el archivo .ui
        uic.loadUi("GUI/ui_sudoku_solver.ui", self)
        self.make_board()
        self.set_style()

        self.solve_button.clicked.connect(self.solve)

    def get_board(self):
        """
        Obtiene los valores ingresados por el usuario en el tablero.

        Salida:
            Una lista de listas que representa el tablero de Sudoku.
        """

        # Se crea una matriz vacía de 9x9
        b = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                # Se obtiene el número ingresado en la caja de texto correspondiente
                numero = self.board[i][j].text()
                # Si la caja de texto no está vacía
                if numero != "":
                    # Se agrega el número a la matriz
                    b[i][j] = int(numero)

        # Se devuelve la matriz de números
        return b

    def set_style(self):
        """
        Configura el estilo de los QLineEdit en el tablero.
        """

        for i in range(9):
            for j in range(9):
                # Se centra el texto de la caja de texto
                self.board[i][j].setAlignment(QtCore.Qt.AlignCenter)
                # Se establece la longitud máxima de la entrada en 1
                self.board[i][j].setMaxLength(1)
                # Se conecta la señal textChanged al método check_number
                self.board[i][j].textChanged.connect(lambda _, i=i, j=j: self.check_number(i, j))
    
    
    def check_number(self, i, j):
        """
        Verifica si un número ingresado en el Sudoku es válido o no.
        Si no es válido, se marca la caja de texto en rojo.

        Entrada:
            i: La fila del número en el tablero.
            j: La columna del número en el tablero.
        """
        # Se marca la caja de texto en negro 
        self.board[i][j].setStyleSheet("color: black; background-color: " + self.board[i][j].palette().color(QtGui.QPalette.Base).name())
        # Se obtiene el número ingresado en la caja de texto correspondiente
        numero = self.board[i][j].text()
        # Si la caja de texto no está vacía
        if numero != "":
            # Se convierte el número a entero
            numero = int(numero)
            pos = i, j
            # Se verifica si el número es válido en el tablero actual
            if not is_valid_move(self.get_board(), pos, numero):
                # Si el número no es válido, se marca la caja de texto en rojo
                self.board[i][j].setStyleSheet("color: red; background-color: " + self.board[i][j].palette().color(QtGui.QPalette.Base).name())

    def set_board(self, new_board):
        """
        Establece los valores en el tablero de la aplicación.

        Entrada:
            new_board: Una lista de listas que representa el tablero de
            Sudoku solucionado.
        """

        for i in range(9):
            for j in range(9):
                # Se establece el texto correspondiente con el número de la matriz
                self.board[i][j].setText(str(new_board[i][j]))

    def make_board(self):
        """
        Crea una lista de listas que representa el tablero de Sudoku de la aplicación.
        """

        # Se crea una lista vacía
        self.board = []
        for i in range(9):
            row = []
            for j in range(9):
                # Se obtiene la caja de texto según el nombre del atributo
                row.append(self.__getattribute__(f"line_edit_pos{i}{j}"))
            # Se agrega la lista de cajas de texto a la lista principal
            self.board.append(row)

    def solve(self):
        """
        Resuelve el tablero de Sudoku y establece los valores en la aplicación.
        """

        board = self.get_board()
        if is_valid_board(board):
            solved_board = solve(board)
            self.set_board(solved_board)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("El tablero ingresado no es válido.")
            msg.setWindowTitle("Error")
            msg.exec_()

def main():
    """
    Función principal que inicializa la aplicación.
    """
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

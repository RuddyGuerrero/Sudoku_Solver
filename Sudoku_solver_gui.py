import sys

from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QFont

class MainWindow(QtWidgets.QDialog):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('GUI/ui_sudoku_solver_.ui', self)
        self.make_board()
        self.set_style()

        board_ = [['2'] * 9 for _ in range(9)]
        self.set_board(board_) 


    def set_style(self):
       
        for i in range(9):
            for j in range(9):
                self.board[i][j].setAlignment(QtCore.Qt.AlignCenter)  
                self.board[i][j].setMaxLength(1)
                self.board[i][j].setFont(QFont('Arial', 10))

    def set_board(self, new_board):
        for i in range(9):
            for j in range(9):
                self.board[i][j].setText(str(new_board[i][j]))  

    def make_board(self):
        self.board = [[None] * 9 for _ in range(9)]
        self.board[0][0] = self.line_edit_pos00
        self.board[0][1] = self.line_edit_pos01
        self.board[0][2] = self.line_edit_pos02
        self.board[0][3] = self.line_edit_pos03
        self.board[0][4] = self.line_edit_pos04
        self.board[0][5] = self.line_edit_pos05
        self.board[0][6] = self.line_edit_pos06
        self.board[0][7] = self.line_edit_pos07
        self.board[0][8] = self.line_edit_pos08

        self.board[1][0] = self.line_edit_pos10
        self.board[1][1] = self.line_edit_pos11
        self.board[1][2] = self.line_edit_pos12
        self.board[1][3] = self.line_edit_pos13
        self.board[1][4] = self.line_edit_pos14
        self.board[1][5] = self.line_edit_pos15
        self.board[1][6] = self.line_edit_pos16
        self.board[1][7] = self.line_edit_pos17
        self.board[1][8] = self.line_edit_pos18

        self.board[2][0] = self.line_edit_pos20
        self.board[2][1] = self.line_edit_pos21
        self.board[2][2] = self.line_edit_pos22
        self.board[2][3] = self.line_edit_pos23
        self.board[2][4] = self.line_edit_pos24
        self.board[2][5] = self.line_edit_pos25
        self.board[2][6] = self.line_edit_pos26
        self.board[2][7] = self.line_edit_pos27
        self.board[2][8] = self.line_edit_pos28

        self.board[3][0] = self.line_edit_pos30
        self.board[3][1] = self.line_edit_pos31
        self.board[3][2] = self.line_edit_pos32
        self.board[3][3] = self.line_edit_pos33
        self.board[3][4] = self.line_edit_pos34
        self.board[3][5] = self.line_edit_pos35
        self.board[3][6] = self.line_edit_pos36
        self.board[3][7] = self.line_edit_pos37
        self.board[3][8] = self.line_edit_pos38

        self.board[4][0] = self.line_edit_pos40
        self.board[4][1] = self.line_edit_pos41
        self.board[4][2] = self.line_edit_pos42
        self.board[4][3] = self.line_edit_pos43
        self.board[4][4] = self.line_edit_pos44
        self.board[4][5] = self.line_edit_pos45
        self.board[4][6] = self.line_edit_pos46
        self.board[4][7] = self.line_edit_pos47
        self.board[4][8] = self.line_edit_pos48

        self.board[5][0] = self.line_edit_pos50
        self.board[5][1] = self.line_edit_pos51
        self.board[5][2] = self.line_edit_pos52
        self.board[5][3] = self.line_edit_pos53
        self.board[5][4] = self.line_edit_pos54
        self.board[5][5] = self.line_edit_pos55
        self.board[5][6] = self.line_edit_pos56
        self.board[5][7] = self.line_edit_pos57
        self.board[5][8] = self.line_edit_pos58

        self.board[6][0] = self.line_edit_pos60
        self.board[6][1] = self.line_edit_pos61
        self.board[6][2] = self.line_edit_pos62
        self.board[6][3] = self.line_edit_pos63
        self.board[6][4] = self.line_edit_pos64
        self.board[6][5] = self.line_edit_pos65
        self.board[6][6] = self.line_edit_pos66
        self.board[6][7] = self.line_edit_pos67
        self.board[6][8] = self.line_edit_pos68

        self.board[7][0] = self.line_edit_pos70
        self.board[7][1] = self.line_edit_pos71
        self.board[7][2] = self.line_edit_pos72
        self.board[7][3] = self.line_edit_pos73
        self.board[7][4] = self.line_edit_pos74
        self.board[7][5] = self.line_edit_pos75
        self.board[7][6] = self.line_edit_pos76
        self.board[7][7] = self.line_edit_pos77
        self.board[7][8] = self.line_edit_pos78

        self.board[8][0] = self.line_edit_pos80
        self.board[8][1] = self.line_edit_pos81
        self.board[8][2] = self.line_edit_pos82
        self.board[8][3] = self.line_edit_pos83
        self.board[8][4] = self.line_edit_pos84
        self.board[8][5] = self.line_edit_pos85
        self.board[8][6] = self.line_edit_pos86
        self.board[8][7] = self.line_edit_pos87
        self.board[8][8] = self.line_edit_pos88


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
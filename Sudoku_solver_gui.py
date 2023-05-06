import sys

from PyQt5 import QtWidgets, uic

class MainWindow(QtWidgets.QDialog):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('GUI/ui_sudoku_solver_.ui', self)
        self.board = [[0] * 9 for _ in range(9)]   
        for i in range(9):
            for j in range(9):
                self.board[i][j] = i*9 + j
        self.draw_sudoku()
        

    def draw_sudoku(self):

        self.textEdit_pos00.setText(str(self.board[0][0]))
        self.textEdit_pos01.setText(str(self.board[0][1]))
        self.textEdit_pos02.setText(str(self.board[0][2]))
        self.textEdit_pos10.setText(str(self.board[1][0]))
        self.textEdit_pos11.setText(str(self.board[1][1]))
        self.textEdit_pos12.setText(str(self.board[1][2]))
        self.textEdit_pos20.setText(str(self.board[2][0]))
        self.textEdit_pos21.setText(str(self.board[2][1]))
        self.textEdit_pos22.setText(str(self.board[2][2]))

        self.textEdit_pos03.setText(str(self.board[0][3]))
        self.textEdit_pos04.setText(str(self.board[0][4]))
        self.textEdit_pos05.setText(str(self.board[0][5]))
        self.textEdit_pos13.setText(str(self.board[1][3]))
        self.textEdit_pos14.setText(str(self.board[1][4]))
        self.textEdit_pos15.setText(str(self.board[1][5]))
        self.textEdit_pos23.setText(str(self.board[2][3]))
        self.textEdit_pos24.setText(str(self.board[2][4]))
        self.textEdit_pos25.setText(str(self.board[2][5]))
        
        self.textEdit_pos06.setText(str(self.board[0][6]))
        self.textEdit_pos07.setText(str(self.board[0][7]))
        self.textEdit_pos08.setText(str(self.board[0][8]))
        self.textEdit_pos16.setText(str(self.board[1][6]))
        self.textEdit_pos17.setText(str(self.board[1][7]))
        self.textEdit_pos18.setText(str(self.board[1][8]))
        self.textEdit_pos26.setText(str(self.board[2][6]))
        self.textEdit_pos27.setText(str(self.board[2][7]))
        self.textEdit_pos28.setText(str(self.board[2][8]))

        self.textEdit_pos30.setText(str(self.board[3][0]))
        self.textEdit_pos31.setText(str(self.board[3][1]))
        self.textEdit_pos32.setText(str(self.board[3][2]))
        self.textEdit_pos40.setText(str(self.board[4][0]))
        self.textEdit_pos41.setText(str(self.board[4][1]))
        self.textEdit_pos42.setText(str(self.board[4][2]))
        self.textEdit_pos50.setText(str(self.board[5][0]))
        self.textEdit_pos51.setText(str(self.board[5][1]))
        self.textEdit_pos52.setText(str(self.board[5][2]))

        self.textEdit_pos33.setText(str(self.board[3][3]))
        self.textEdit_pos34.setText(str(self.board[3][4]))
        self.textEdit_pos35.setText(str(self.board[3][5]))
        self.textEdit_pos43.setText(str(self.board[4][3]))
        self.textEdit_pos44.setText(str(self.board[4][4]))
        self.textEdit_pos45.setText(str(self.board[4][5]))
        self.textEdit_pos53.setText(str(self.board[5][3]))
        self.textEdit_pos54.setText(str(self.board[5][4]))
        self.textEdit_pos55.setText(str(self.board[5][5]))
        
        self.textEdit_pos36.setText(str(self.board[3][6]))
        self.textEdit_pos37.setText(str(self.board[3][7]))
        self.textEdit_pos38.setText(str(self.board[3][8]))
        self.textEdit_pos46.setText(str(self.board[4][6]))
        self.textEdit_pos47.setText(str(self.board[4][7]))
        self.textEdit_pos48.setText(str(self.board[4][8]))
        self.textEdit_pos56.setText(str(self.board[5][6]))
        self.textEdit_pos57.setText(str(self.board[5][7]))
        self.textEdit_pos58.setText(str(self.board[5][8]))

        self.textEdit_pos60.setText(str(self.board[6][0]))
        self.textEdit_pos61.setText(str(self.board[6][1]))
        self.textEdit_pos62.setText(str(self.board[6][2]))
        self.textEdit_pos70.setText(str(self.board[7][0]))
        self.textEdit_pos71.setText(str(self.board[7][1]))
        self.textEdit_pos72.setText(str(self.board[7][2]))
        self.textEdit_pos80.setText(str(self.board[8][0]))
        self.textEdit_pos81.setText(str(self.board[8][1]))
        self.textEdit_pos82.setText(str(self.board[8][2]))

        self.textEdit_pos63.setText(str(self.board[6][3]))
        self.textEdit_pos64.setText(str(self.board[6][4]))
        self.textEdit_pos65.setText(str(self.board[6][5]))
        self.textEdit_pos73.setText(str(self.board[7][3]))
        self.textEdit_pos74.setText(str(self.board[7][4]))
        self.textEdit_pos75.setText(str(self.board[7][5]))
        self.textEdit_pos83.setText(str(self.board[8][3]))
        self.textEdit_pos84.setText(str(self.board[8][4]))
        self.textEdit_pos85.setText(str(self.board[8][5]))
        
        self.textEdit_pos66.setText(str(self.board[6][6]))
        self.textEdit_pos67.setText(str(self.board[6][7]))
        self.textEdit_pos68.setText(str(self.board[6][8]))
        self.textEdit_pos76.setText(str(self.board[7][6]))
        self.textEdit_pos77.setText(str(self.board[7][7]))
        self.textEdit_pos78.setText(str(self.board[7][8]))
        self.textEdit_pos86.setText(str(self.board[8][6]))
        self.textEdit_pos87.setText(str(self.board[8][7]))
        self.textEdit_pos88.setText(str(self.board[8][8]))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
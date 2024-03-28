
from mimetypes import init
from shutil import move
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from tictacToe import Ui_MainWindow
from homemenu import Ui_Dialog
from about import Ui_Dialoga
from minimaxx import MoveX
from minmaxo import MoveO
import sys




class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.fn(*self.args, **self.kwargs)


class HomeDlg(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        
        self.o_color.setStyleSheet("")
        self.o_color.clicked.connect(lambda x:self.configureColor(self.o_color))
        self.x_color.clicked.connect(lambda x:self.configureColor(self.x_color))
    
    def configureColor(self,button):
        dlg = QColorDialog(self.parent)
        dlg.exec_()
        self.color =dlg.selectedColor().getRgb()
        back = "QPushButton"+" "+"{"+"background-color:"+"rgb"+str(self.color[0:-1])+";"+"}" 
        button.setStyleSheet(back)
        


class About(QDialog,Ui_Dialoga):
    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(self)


class Window(QMainWindow,Ui_MainWindow):
    oChanged = pyqtSignal(str)
    xChanged = pyqtSignal(str)
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Tic Tac Toe")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.threadmanager = QThreadPool()

        self.buttons = {1:self.pushButton_1,2:self.pushButton_2,3:self.pushButton_3,
                        4:self.pushButton_4,5:self.pushButton_5,6:self.pushButton_6,
                        7:self.pushButton_7,8:self.pushButton_8,9:self.pushButton_9}
        self.board = {1:self.pushButton_1.text(), 2:self.pushButton_2.text(), 3:self.pushButton_3.text(),
                      4:self.pushButton_4.text(),5:self.pushButton_5.text(), 6:self.pushButton_6.text(),
                      7:self.pushButton_7.text(), 8:self.pushButton_8.text(),9:self.pushButton_9.text()}
        self.initializeValues()
        self.pushButton_1.clicked.connect(lambda x: self.play(self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda x:self.play(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda x:self.play(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda x:self.play(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda x:self.play(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda x:self.play(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda x:self.play(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda x:self.play(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda x:self.play(self.pushButton_9))
        self.actionQuit.triggered.connect(self.close)
        self.actionHome.triggered.connect(self.showSettings)
        self.actionReset.triggered.connect(self.resetBoard)
        self.actionReset_2.triggered.connect(self.resetBoard)
        self.actionAbout.triggered.connect(self.about)
        self.action_Save.triggered.connect(self.saveGame)
        self.action_Find_Next_move.triggered.connect(self.findBestMove)
 
    def checkWin(self):
        if (self.buttons[1].text() == self.buttons[2].text() and self.buttons[1].text() == self.buttons[3].text() and self.buttons[1].text()!=""):
                self.highlight(self.buttons[1],self.buttons[2],self.buttons[3])
                return True
        if (self.buttons[4].text() == self.buttons[5].text() and self.buttons[4].text() == self.buttons[6].text() and self.buttons[4].text()!=""):
            self.highlight(self.buttons[4],self.buttons[5],self.buttons[6])
            return True
        if (self.buttons[7].text() == self.buttons[8].text() and self.buttons[7].text() == self.buttons[9].text() and self.buttons[7].text()!=""):
            self.highlight(self.buttons[7],self.buttons[8],self.buttons[9])
            return True
        if (self.buttons[1].text() == self.buttons[4].text() and self.buttons[1].text() == self.buttons[7].text() and self.buttons[1].text()!=""):
            self.highlight(self.buttons[1],self.buttons[4],self.buttons[7])
            return True
        if (self.buttons[2].text() == self.buttons[5].text() and self.buttons[2].text() == self.buttons[8].text() and self.buttons[2].text()!=""):
            self.highlight(self.buttons[2],self.buttons[5],self.buttons[8])
            return True
        if (self.buttons[3].text() == self.buttons[6].text() and self.buttons[3].text() == self.buttons[9].text() and self.buttons[3].text() !=""):
            self.highlight(self.buttons[3],self.buttons[6],self.buttons[9])
            return True
        if (self.buttons[1].text() == self.buttons[5].text() and self.buttons[1].text() == self.buttons[9].text() and self.buttons[1].text()!="" ):
            self.highlight(self.buttons[1],self.buttons[5],self.buttons[9])
            return True
        if (self.buttons[7].text() == self.buttons[5].text() and self.buttons[7].text() == self.buttons[3].text() and self.buttons[7].text()!="" ):
            self.highlight(self.buttons[7],self.buttons[5],self.buttons[3])
            return True
        else:
            return False
        
    def initializeValues(self):
            self.sound = True
            self.playwith = "X"
            self.mode = "Against"
            self.automaticallyReset = False
            self.xColor = QColor("black")
            self.oColor = QColor("black")
            self.markerSize = 15
            self.showMoves = True
            self.count = 1

        
    def isOver(self):
            if self.checkWin() or self.checkDraw():
                return True
            return False


    def highlight(self,btn1,btn2,btn3):
        btns = [btn1,btn2,btn3]
        for btn in btns:
            btn.setStyleSheet("QPushButton {background-color:red}")
            for btn in self.buttons.keys():
                self.buttons[btn].setEnabled(False)
        self.movesScreen.insertHtml(f" <html> <p style='color:red;font-weight:bold;font-size:19px;text-decoration:underline'> &nbsp;&nbsp;{btn1.text()} Won </p> </html>")
        msg = QMessageBox.about(self, "Tic Tac Toe", f"{btn1.text()} has Won")

    def checkDraw(self, popup=True):
        for button in self.buttons.keys():
            if self.buttons[button].text() == "":
                return False
        if popup==True:
            msg = QMessageBox.about(self, "Tic Tac Toe", "this match is a tight!")
        return True

    def initGame(self):
        pass
    def insertO(self,board):
        pass
    def insertX(self,board):
        pass
    def insertMark(self,mark,btn):
        if not self.checkWin():
            self.player = QMediaPlayer()
            self.file = QUrl.fromLocalFile("ES_Mouse Click 3 - SFX Producer.mp3")
            content = QMediaContent(self.file)
            self.player.setMedia(content)
            self.player.play()
            btn.setText(mark)
            btn.setEnabled(False)
            self.movesScreen.moveCursor(QTextCursor.End)
            self.movesScreen.insertPlainText(f" {mark}:{btn.objectName()[-1]} ")
            if not self.checkWin():
                self.checkDraw()
                
            
    def gameMode(self):
        pass
    def multiplayer(self,button):
        if not self.checkWin():
            if self.count % 2 != 0:
                self.insertMark(self.playwith,button)
            else:
                sign  = "X" if self.playwith=="O" else "O"
                self.insertMark(sign,button)
        self.count +=1
    def Board(self):
        board = dict(zip(range(1,10), [b.text() for b in self.buttons.values()]))
        return board
        
    def computerMove(self,mark,board):
        if not self.checkDraw(popup=False):
            if mark == "X":
                if not self.checkWin():
                    move = MoveX(board).FindMove()
                    print("X",move)
                    self.movesScreen.moveCursor(QTextCursor.End)
                    self.movesScreen.insertPlainText(f" {mark}:{self.buttons[move].objectName()[-1]} ")
                    self.buttons[move].setText(mark)
                    self.buttons[move].setEnabled(False)
                    return move
            if mark == "O":
                if not self.checkWin():
                        move = MoveO(board).FindMove()
                        print("O",move)
                        self.movesScreen.moveCursor(QTextCursor.End)
                        self.movesScreen.insertPlainText(f" {mark}:{self.buttons[move].objectName()[-1]} ")
                        self.buttons[move].setText(mark)
                        self.buttons[move].setEnabled(False)
                        return move

    def onlyComputerMoves(self,move):
        if isinstance(move,str) and move !="None":
            self.buttons[int(move)].setText(move)

    def userMove(self):
        pass

    def playComputerOnly(self):
        worker = Worker(self.onlyComputer)
        self.threadmanager.start(worker)


    def onlyComputer(self):
        while not self.checkDraw():
            board = self.Board()
            print(board)
            movex = self.computerMove("X",board)
            self.xChanged.emit(f"{movex}")
            board2 = self.Board()
            moveo = self.computerMove("O",board2)
            self.oChanged.emit(f"{moveo}")



    def againstComputer(self,button):
        if not self.checkWin():
            self.insertMark(self.playwith,button)

        if not self.checkWin():
            if not self.checkDraw(popup=False):
                board = self.Board()
                sign  = "X" if self.playwith =="O" else "O"
                self.computerMove(sign,board)
                self.checkWin()
                    
    def play(self, button):
        gamemode = self.mode
        self.reset = self.automaticallyReset
        if gamemode=="multi":
            self.multiplayer(button)
        elif gamemode=="OnlyComputer":
            self.onlyComputer(button)
        elif gamemode=="Against":
            self.againstComputer(button)
    
    def findBestMove(self):
        board = self.Board()
        move = MoveX(board).FindMove()
        msg = QMessageBox.about(self,"Best Move", f"the best move in this position is: {move}")

    def resetBoard(self):
        for button in self.buttons.keys():
            self.buttons[button].setEnabled(True)
            self.buttons[button].setText("")
            self.buttons[button].setStyleSheet("")
        self.movesScreen.clear()
        self.setMovesScreenHTML()
        self.count = 1

    def showSettings(self):
        dlg = HomeDlg(self)
        dlg.exec_()

    def about(self):
        dlg = About(self)
        dlg.exec_()  
    

    def closeEvent(self,event):
        question = QMessageBox.question(self,"Tic Tac Toe", "Do you want to quit?")
        if question==QMessageBox.Yes:
            event.accept()
            sys.exit()
        else:
            event.ignore()

    def contextMenuEvent(self, event):
        pass
    def saveGame(self):
        #file = QFileDialog.getOpenFileName(self,"Save",None,"JSON (*.json)")
        file = 0
        moves = self.movesScreen.toPlainText().split()
        words = ["Moves:", "X","Won", "O"]
        moves = [move for move in moves if move not in words]
        moves = dict(enumerate(moves))
        print(moves)
        
        

    def setMovesScreenHTML(self):
        self.movesScreen.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; text-decoration: underline; color:#005500;\">Moves:</span><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#005500;\">   </span></p></body></html>")  

app = QApplication([])
window = Window()
window.show()
app.exec_()









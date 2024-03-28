

class MoveX():
    def __init__(self,buttons):
        self.x = "X"
        self.o = "O"
        super().__init__()
        self.buttons = buttons

        ["","",""]
        ["","",""]
        ["","",""]

    def CheckWin(self,mark):
        if (self.buttons[1] == self.buttons[2] and self.buttons[1] == self.buttons[3] and self.buttons[1] == mark):
            return True
        if (self.buttons[4] == self.buttons[5] and self.buttons[4] == self.buttons[6] and self.buttons[4] == mark):
            return True
        if (self.buttons[7] == self.buttons[8] and self.buttons[7] == self.buttons[9] and self.buttons[7] == mark):
            return True
        if (self.buttons[1] == self.buttons[4] and self.buttons[1] == self.buttons[7] and self.buttons[1] == mark):
            return True
        if (self.buttons[2] == self.buttons[5] and self.buttons[2] == self.buttons[8] and self.buttons[2] == mark):
            return True
        if (self.buttons[3] == self.buttons[6] and self.buttons[3] == self.buttons[9] and self.buttons[3] == mark):
            return True
        if (self.buttons[1] == self.buttons[5] and self.buttons[1] == self.buttons[9] and self.buttons[1] == mark):
            return True
        if (self.buttons[7] == self.buttons[5] and self.buttons[7] == self.buttons[3] and self.buttons[7] == mark):
            return True
        else:
            return False

    def CheckDraw(self):
        for key in self.buttons.keys():
            if self.buttons[key] == "":
                return False
        return True

    def MiniMax(self,board,ismax):
        if self.CheckWin(self.x):
            return 1
        if self.CheckWin(self.o):
            return -1
        if self.CheckDraw():
            return 0
        if ismax:
            bestScore = -800
            for key in board.keys():
                if board[key]=="":
                    board[key]=self.x
                    score = self.MiniMax(board,False)
                    board[key]=""
                    if score>bestScore:
                        bestScore = score
            return bestScore
        else:
            bestScore = 800
            for key in board.keys():
                if board[key]=="":
                    board[key]=self.o
                    score = self.MiniMax(board,True)
                    board[key]=""
                    if score<bestScore:
                        bestScore = score
            return bestScore

    def FindMove(self):
        bestScore = -800
        bestMove = 0
        for key in self.buttons.keys():
            if self.buttons[key] == "":
                self.buttons[key] = self.x
                score = self.MiniMax(self.buttons,False)
                self.buttons[key] = ""
                if score > bestScore:
                    bestScore = score
                    bestMove = key
        return bestMove
   

    
board = {1: '', 2: '', 3: '',
         4: '', 5: '', 6: '',
         7: '', 8: '', 9: ''}




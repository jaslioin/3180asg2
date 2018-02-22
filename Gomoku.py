
class Gomoku:
    gameBoard = [[" " for x in range(10)] for y in range(10)]
    player1=1
    player2=2
    turn = 1
    MAX_TURN = 81
    def __init__(self):
        self.turn = 1
        self.createPlayer('O',self.player1)
        self.createPlayer('X',self.player2)
    def startGame(self):
        win = False
        turncount = 0
        print("game start!!")
        while(win==False):

            print "********* turn",turncount,"*********"
            if(self.turn == 1):
                print "player O's turn"
                self.player1.nextMove()
                self.turn=2
            else:
                print "player X's turn"
                self.player2.nextMove()
                self.turn=1
            win = self.checkWin()
            turncount = turncount+1
            self.printGameBoard()
            if(turncount == self.MAX_TURN):
                if(self.checkTie()==True):
                    print "TIE"
                    exit(0)
        else:
            print("player %d wins" % hashtable[self.gameBoard[lastIndex[0]][lastIndex[1]]])
    def printGameBoard(self):
        counter = 1
        print "#|",
        for i in range(1, 10):
            print("%d |" % i),
        print ""

        for i in self.gameBoard:
            printrow()
            if (counter > 9):
                break
            printcol(counter)

            for j in range(1,10):
                print ("%s |" % self.gameBoard[counter][j]),
            counter = counter + 1
            print ""

    def checkWin(self):

        symbol = self.gameBoard[lastIndex[0]][lastIndex[1]]

        # check left-right X,y+/-
        contiguousSymbol = 0
        for y in self.gameBoard[lastIndex[0]]:
            if y == symbol:
                contiguousSymbol += 1
            else:
                contiguousSymbol = 0
            if contiguousSymbol == 5:
                return True
        # check up-down x+/-,Y
        counter=0
        contiguousSymbol = 0
        while(counter<10):
            if self.gameBoard[counter][lastIndex[1]] == symbol:
                contiguousSymbol += 1
            else:
                contiguousSymbol = 0
            if contiguousSymbol == 5:
                return True
            counter+=1
        # check topleft-bottomright x--/x++ y--/y++
            contiguousSymbol = 0
            x=lastIndex[0]
            y=lastIndex[1]
            while(x>1 and y>1):
                x -= 1
                y -= 1
            while(x<10 and y<10):
                if self.gameBoard[x][y] == symbol:
                    contiguousSymbol += 1
                else:
                    contiguousSymbol = 0
                if contiguousSymbol ==5 :
                    return True
                x += 1
                y += 1
        # check bottomleft-topright x++/x--,y--/y++
            contiguousSymbol = 0
            x = lastIndex[0]
            y = lastIndex[1]
            while (x > 1 and y < 10):
                x -= 1
                y += 1
            while (x < 10 and y >= 1):
                if self.gameBoard[x][y] == symbol:
                    contiguousSymbol += 1
                else:
                    contiguousSymbol = 0
                if contiguousSymbol == 5:
                    return True
                x += 1
                y -= 1

        if contiguousSymbol < 5:
            return False






    def checkTie(self):
        if( self.checkWin() == False ):
            return True
    def createPlayer(self,symbol,playerNum):
        if(symbol == 'O'):
            print "please choose player 1(O)"
            print "1. Human"
            print "2. Computer"
            choosetype = int(raw_input("your choice: "))
            if choosetype == 1:
                self.player1 = Human(symbol,self.gameBoard,False,1)
                print("Player O is Human")
            else:
                self.player1 = Computer(symbol, self.gameBoard,True,1)
                print("Player O is Computer")
        elif(symbol == 'X'):
            print "please choose player 2(X)"
            print "1. Human"
            print "2. Computer"
            choosetype = int(raw_input("your choice: "))
            if choosetype == 1:
                self.player2 = Human(symbol, self.gameBoard,False,1)
                print("Player X is Human")
            else:
                self.player2 = Computer(symbol, self.gameBoard,True,1)
                print("Player X is Computer")


class Player(object):
    gameBoard = [[0 for x in range(1, 10)] for y in range(1, 10)]
    playerSymbol = 1
    isPC=False
    def __init__(self, symbol , gameboard,isPC):
        self.playerSymbol = symbol
        self.gameBoard = gameboard
        self.isPC = isPC

    def nextMove(self):
        pass


class Human(Player):
    humanstuff ='im human'
    def __init__(self,symbol,gameboard,isPC,humanstuff):
        super(Human,self).__init__(symbol, gameboard,isPC)
        self.humanstuff=humanstuff
    def nextMove (self):
        while(True):
            print "input target row column(1~9)",
            row, col = map(int, raw_input().split())
            if row>9 or row<1 or col > 9 or col < 1:
                print "value out of range(1~9)"
            else:
                break

        if self.gameBoard[row][col] == " ":
            print "tuple is empty"
            self.gameBoard[row][col]=self.playerSymbol
            lastIndex[0]=row
            lastIndex[1]=col
            print("placed %s at %d,%d" %(self.playerSymbol,row,col))
        else:
            print "tuple is occupied"
            self.nextMove()
class Computer(Player):
    computerstuff='im pc'
    def __init__(self,symbol,gameboard,isPC,computerstuff):
        super(Computer,self).__init__(symbol, gameboard,isPC)
        self.computerstuff=computerstuff
    def nextMove(self):
        print "hey i cant move yet"
def printrow():
    #print '-------------------------------------'
    print '______________________________________'
def printcol(colno):
    print ("%d|" %(colno)),

# initialize game grid
# choose player

game = Gomoku()
game.printGameBoard()
lastIndex=[0,0]
hashtable={"O": 1,"X": 2}
game.startGame()









# game loop

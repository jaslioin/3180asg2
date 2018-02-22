class Gomoku:
    gameBoard = [[" " for x in range(9)] for y in range(9)]
    player1=1
    player2=2
    turn = 0
    def __init__(self):
        self.turn = 0
        self.player1
        self.player2

        self.createPlayer('O',self.player1)
        self.createPlayer('X',self.player2)
    def startGame(self):
        while(1):
            print("game start!!")
            break
    def printGameBoard(self):
        counter = 0
        print "#|",
        for i in range(1, 10):
            print("%d |" % i),
        print ""
        for i in self.gameBoard:
            printrow()
            if (counter >= len(self.gameBoard)):
                break
            printcol(counter)
            for j in self.gameBoard[counter]:
                print ("%s |" % j),
            counter = counter + 1
            print ""

    def checkWin(self):
        print 'hi'
    def checkTie(self):
        print 'hi'
    def createPlayer(self,symbol,playerNum):
        if(symbol == 'O'):
            print "please choose player 1(O)"
            print "1. Human"
            print "2. Computer"
            choosetype = int(raw_input("your choice: "))
            if choosetype == 1:
                self.player1 = Human(symbol,self.gameBoard,1)
                print("Player O is Human")
            else:
                self.player1 = Computer(symbol, self.gameBoard,1)
                print("Player O is Computer")
        elif(symbol == 'X'):
            print "please choose player 2(X)"
            print "1. Human"
            print "2. Computer"
            choosetype = int(raw_input("your choice: "))
            if choosetype == 1:
                self.player2 = Human(symbol, self.gameBoard,1)
                print("Player X is Human")
            else:
                self.player2 = Computer(symbol, self.gameBoard,1)
                print("Player X is Computer")


class Player(object):
    gameBoard = [[0 for x in range(9)] for y in range(9)]
    playerSymbol = 1

    def __init__(self, symbol , gameboard):
        self.playerSymbol = symbol
        self.gameBoard = gameboard

    def nextMove(self):
        pass


class Human(Player):
    humanstuff ='im human'
    def __init__(self,symbol,gameboard,humanstuff):
        super(Human,self).__init__(symbol, gameboard)
        self.humanstuff=humanstuff
    def nextMove(self):
        row = int(raw_input("target row: "))
        col = int(raw_input("target column: "))
        if(self.gameBoard[row][col] ==" "):
            print "index is empty"
            self.gameBoard[row][col]=self.playerSymbol
        else:
            print "not empty ar!!!"

class Computer(Player):
    computerstuff='im pc'
    def __init__(self,symbol,gameboard,computerstuff):
        super(Computer,self).__init__(symbol, gameboard)
        self.computerstuff=computerstuff

def printrow():
    #print '-------------------------------------'
    print '______________________________________'
def printcol(colno):
    print ("%d|" %(colno+1)),

# initialize game grid
# choose player
game = Gomoku()
game.printGameBoard()

game.player1.nextMove()









# game loop

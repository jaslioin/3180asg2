class Gomoku:
    gameBoard = [[0 for x in range(9)] for y in range(9)]
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
        print 'hi'
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
        print "place at grid x y"

class Human(Player):
    humanstuff ='im human'
    def __init__(self,symbol,gameboard,humanstuff):
        super(Human,self).__init__(symbol, gameboard)
        self.humanstuff=humanstuff

class Computer(Player):
    computerstuff='im pc'
    def __init__(self,symbol,gameboard,computerstuff):
        super(Computer,self).__init__(symbol, gameboard)
        self.computerstuff=computerstuff


# initialize game grid
# choose player
 game = Gomoku()







game.gameBoard[1][1]=1
game.gameBoard[0][0]=0
game.gameBoard[8][8]=8
game.gameBoard[8][7]=87
for i in game.gameBoard:
   print i






# game loop

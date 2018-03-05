# CSCI3180 Principles of Programming Languages
# --- Declaration ---
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
# Assignment 2
# Name : Li Ho Yin
#Student ID : 1155077785
#Email Addr : hyli6@cse.cuhk.edu.hk
# cite
# 2 input split by space : https://stackoverflow.com/questions/23253863/how-to-input-2-integers-in-one-line-in-python
# 2d list : https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python

import random


class Gomoku:

    def __init__(self):
        self.gameBoard = [[" " for x in range(10)] for y in range(10)]
        self.player1 = 1
        self.player2 = 2
        self.turn = 1
        self.MAX_TURN = 81
        self.createPlayer('O', self.player1)
        self.createPlayer('X', self.player2)

    def startGame(self):
        win = False
        turncount = 0
        print("game start!!")
        while (win == False):

            print "********* turn", turncount, "*********"
            if (self.turn == 1):
                print "player O's turn"
                self.player1.nextMove()
                self.turn = 2
            else:
                print "player X's turn"
                self.player2.nextMove()
                self.turn = 1
            win = self.checkWin()
            turncount = turncount + 1
            self.printGameBoard()
            if (turncount == self.MAX_TURN):
                if(self.checkTie()==True):
                    print "***** TIE *****"
                    exit(0)
        else:
            print("***** player %d wins *****" % hashtable[self.gameBoard[lastIndex[0]][lastIndex[1]]])

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

            for j in range(1, 10):
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
        counter = 0
        contiguousSymbol = 0
        while (counter < 10):
            if self.gameBoard[counter][lastIndex[1]] == symbol:
                contiguousSymbol += 1
            else:
                contiguousSymbol = 0
            if contiguousSymbol == 5:
                return True
            counter += 1
            # check topleft-bottomright x--/x++ y--/y++
            contiguousSymbol = 0
            x = lastIndex[0]
            y = lastIndex[1]
            while (x > 1 and y > 1):
                x -= 1
                y -= 1
            while (x < 10 and y < 10):
                if self.gameBoard[x][y] == symbol:
                    contiguousSymbol += 1
                else:
                    contiguousSymbol = 0
                if contiguousSymbol == 5:
                    return True
                x += 1
                y += 1
            # check bottomleft-topright x++/x--,y--/y++
            contiguousSymbol = 0
            x = lastIndex[0]
            y = lastIndex[1]
            while (x > 1 and y < 9):
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
        if (self.checkWin() == False):
            return True

    def createPlayer(self, symbol, playerNum):
        if (symbol == 'O'):
            print "please choose player 1(O)"
            print "1. Human"
            print "2. Computer"
            while (True):
                choosetype = int(raw_input("your choice: "))
                if (choosetype in [1, 2]):
                    break
                else:
                    print "***** print enter 1 or 2 *****"
            if choosetype == 1:
                self.player1 = Human(symbol, self.gameBoard)
                print("Player O is Human")
            else:
                self.player1 = Computer(symbol, self.gameBoard)
                print("Player O is Computer")
        elif (symbol == 'X'):
            print "please choose player 2(X)"
            print "1. Human"
            print "2. Computer"
            while (True):
                choosetype = int(raw_input("your choice: "))
                if (choosetype in [1, 2]):
                    break
                else:
                    print "***** print enter 1 or 2 *****"
            if choosetype == 1:
                self.player2 = Human(symbol, self.gameBoard)
                print("Player X is Human")
            else:
                self.player2 = Computer(symbol, self.gameBoard)
                print("Player X is Computer")


class Player(object):
    gameBoard = [[0 for x in range(10)] for y in range(10)]
    playerSymbol = 1

    def __init__(self, symbol, gameboard):
        self.playerSymbol = symbol
        self.gameBoard = gameboard

    def nextMove(self):
        pass


class Human(Player):
    def __init__(self, symbol, gameboard):
        super(Human, self).__init__(symbol, gameboard)

    def nextMove(self):
        localturncount = 0
        tried = [[0 for x in range(10)] for y in range(10)]
        while (True):
            while (True):
                try:
                    print "input target row column(1~9)",
                    row, col = map(int, raw_input().split())
                    if row > 9 or row < 1 or col > 9 or col < 1:
                        print "***** value out of range(1~9) *****"
                    else:
                        break
                except ValueError as ve:
                    print "***** please input row column on same line *****"
            if(tried[row][col] == 1):
                print "you already tried %d %d" %(row,col)
                continue

            if self.gameBoard[row][col] == " ":
                print "***** tuple is empty *****"
                self.gameBoard[row][col] = self.playerSymbol
                lastIndex[0] = row
                lastIndex[1] = col
                print("placed %s at %d,%d" % (self.playerSymbol, row, col))
                break
            else:
                print "***** tuple is occupied *****"
                tried[row][col] = 1
                localturncount += 1
                if (localturncount >= 5):
                    break
                continue


class Computer(Player):
    def __init__(self, symbol, gameboard):
        super(Computer, self).__init__(symbol, gameboard)


    def nextMove(self):
        localturncount = 0
        tried = [[0 for x in range(10)] for y in range(10)]
        while (True):
            row = random.randrange(1, 10)
            col = random.randrange(1, 10)
            if(tried[row][col]==1):
                continue
            if self.gameBoard[row][col] == " ":
                print "***** tuple is empty *****"
                self.gameBoard[row][col] = self.playerSymbol
                lastIndex[0] = row
                lastIndex[1] = col
                print("placed %s at %d,%d" % (self.playerSymbol, row, col))
                break
            else:
                print ("***** tuple %d %d is occupied *****" % (row, col))
                tried[row][col] = 1
                localturncount += 1
                if (localturncount >= 81):
                    break
                continue



def printrow():
    # print '-------------------------------------'
    print '______________________________________'


def printcol(colno):
    print ("%d|" % (colno)),


# initialize game grid
# choose player

game = Gomoku()
game.printGameBoard()
lastIndex = [0, 0]
hashtable = {"O": 1, "X": 2}

game.startGame()

# game loop

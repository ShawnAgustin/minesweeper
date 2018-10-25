import random

"this class is lame"
class Minesweeper:
    def __init__(self):
        self.col = int(input("Enter a length: "))
        self.row = int(input("Enter a height: "))
        self.bomb = int(input("Enter number of bombs (max " + str(self.row *self.col)+ " bombs): "))

        # if number of bombs is invalid it will loop until valid
        while self.bomb > (self.row * self.col) or self.bomb <= 0:
            print("Please enter a valid number of bombs")
            self.bomb = int(input("Enter number of bombs: "))

        # create stack for the game to know which places are bombs and another list for the players choices
        self.boardStack = []
        self.playerStack = []

        # creates a list of placeholders with x # of good spots
        for i in range(self.row):
            for j in range(self.col):
                self.boardStack.append('x')

        # makes space for the amount of bombs in the stack by removing (bombs) # of spots
        self.boardStack = self.boardStack[self.bomb:]

        # adds 'B' to replace the removed x then shuffles the list to randomize list
        for i in range(self.bomb):
            self.boardStack.append('B')
        random.shuffle(self.boardStack)
        print("BoardStack", self.boardStack)

        # fills the playerStack with empty '' strings
        for i in range(self.row * self.col):
            self.playerStack.append('')
        print("PlayerStack", self.playerStack)

        self.print()

        choicex, choicey = self.select()
        index = self.convertCoords(choicex, choicey)
        print(index)
        while True:
            option = input("\"select\" or \"flag\" or \"unflag\"? ")
            if option == "select":
                self.choose(choicex, choicey)
                if self.playerStack[index] == 'B':
                    print("Game Over")
                    break
                else:
                    #if self.checkSurround(choicex,choicey) == 0:
                     #   print("AYYYYYY")
                    #else:
                    self.playerStack[index] = self.checkSurround(choicex, choicey)
                    print(self.playerStack)
            elif option == "flag":
                self.flag(choicex, choicey)
            elif option == "unflag":
                self.unflag(choicex, choicey)

            self.print()
            choicex, choicey = self.select()
            index = self.convertCoords(choicex, choicey)





    def print(self):
        print(" ", end="|  ")
        for i in range(1, self.col+1):
            print(i, end="  |  ")
        print("\n-")
        for j in range(1, self.row+1):
            print(j, end="   ")
            split = self.split(self.playerStack,self.col)
            for row in range(self.col):
                print(split[j-1][row], end="   ")
            print ("\n-")

    def checkValid(self, x, y):
        if self.col < x or self.row < y or x < 0 or y < 0:
            print("Please enter valid coordinates within the range")
            return False
        else:
            return True

    def select(self):
        x = int(input("Select an x coordinate: "))
        y = int(input("Select a y coordinate: "))
        while not self.checkValid(x, y):
            x = int(input("Select an x coordinate: "))
            y = int(input("Select a y coordinate: "))
        return x, y

    def choose(self, x, y):
        selected = self.convertCoords(x, y)
        revealed = self.boardStack[selected]
        if self.playerStack[selected] != '':
            print("This position has already been revealed")
            return
        self.playerStack[selected] = revealed
        #print(self.playerStack)

    def selectFirst(self):
        pass

    def flag(self, x, y):
        selected = self.convertCoords(x, y)
        if self.playerStack[selected] == 'x' or self.playerStack[selected] == 'B':
            print("This position has already been revealed")
            print(self.playerStack)
            return
        self.playerStack[selected] = 'F'
        print(self.playerStack)

    def unflag(self, x, y):
        selected = self.convertCoords(x, y)
        if self.playerStack[selected] == 'x' or self.playerStack[selected] == 'B':
            print("This position has already been revealed")
            print(self.playerStack)
            return
        self.playerStack[selected] = ''
        print(self.playerStack)

    def checkStatus(self):
        pass

    def _getSolution(self):
        pass

    def convertCoords(self, x, y):
        return x - 1 + ((y - 1) * self.col)

    def checkSurround(self, x, y):
        bombs = 0
        x -= 1
        y -= 1
        board = self.split(self.boardStack,self.col)
        # y tells us which list to choose from then x tells us which element within that list we are checking
        checky = [y, y + 1, y - 1]
        checkx = [x , x + 1, x - 1]
        #print(board)
        for y in checky:
            for x in checkx:
                if x < 0 or y < 0 or x >= self.col or y >= self.row:
                    # out of range error messes up the check
                    continue
                else:
                    if board[y][x] == 'B':
                        bombs += 1
                    #print(y, x, board[y][x])
        return bombs


    def split(self, alist, cols):
        oldlist = alist
        sublist = []
        while len(oldlist) != 0:
            newlist = []
            for i in range(cols):
                newlist.append(oldlist[i])
            oldlist = oldlist[cols:]
            sublist.append(newlist)
        return sublist


test = Minesweeper()

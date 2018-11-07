import random

class Minesweeper:
    def __init__(self):
        #self.wins = 0
        #self.loses = 0
        self.status = ''
        #self.start()

        
    def start(self):
        self.col = int(input("Enter a length: "))
        self.row = int(input("Enter a height: "))
        while self.col == 1 and self.row == 1:
            print("Size of board must be larger than 1 square")
            self.col = int(input("Enter a length: "))
            self.row = int(input("Enter a height: "))
        self.bomb = int(input("Enter number of bombs (max " + str(self.row *self.col - 1)+ " bombs): "))


        # if number of bombs is invalid it will loop until valid
        while self.bomb >= (self.row * self.col) or self.bomb <= 0:
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

        # fills the playerStack with empty 'x' strings
        for i in range(self.row * self.col):
            self.playerStack.append('x')
        self.print()

        choicex, choicey = self.select()
        index = self.convertCoords(choicex, choicey)

        
        first = True
        while True:
            option = input("\"[s]elect\" or \"[f]lag\" or \"[u]nflag\"? ").strip()
            option = option.casefold()
            if option == "select" or option == "s":
                if first == True:
                    self.selectFirst(choicex,choicey)
                    first = False
                self.choose(choicex, choicey)
                if self.playerStack[index] == 'B':
                    self.print()
                    self.status = False
                    print("Game Over")
                    break
                elif self.playerStack[index] == 'F':
                    print("This is position is flagged, unflag it if you want to select this position")
                else:
                    if self.checkSurround(choicex,choicey) == 0:
                        show = self.showSurround(choicex,choicey)
                    self.playerStack[index] = self.checkSurround(choicex, choicey)
            elif option == "flag" or option == "f":
                self.flag(choicex, choicey)
            elif option == "unflag" or option == "u":
                self.unflag(choicex, choicey)
            if (self.playerStack.count('x')+self.playerStack.count('F')) == self.boardStack.count('B') :#When you have chosen all spots not a bomb you win
                self.status = True
                print("You win!")
                break
            
            self.print()
            choicex, choicey = self.select()
            index = self.convertCoords(choicex, choicey)

        self._getSolution()

    def print(self):
        print(" ", end="|  ")
        for i in range(1, self.col+1):
            print(i, end="  |  ")
        print("\n-")
        for j in range(1, self.row+1):
            print(j, end="   ")
            split = self.split(self.playerStack,self.col)
            for row in range(self.col):
                print(split[j-1][row], end="     ")
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
        if self.playerStack[selected] == type(int):
            print("This position has already been revealed")
            return
        if self.playerStack[selected] == "F":
            return
        else:
            self.playerStack[selected] = revealed

    def selectFirst(self,x,y):
        while not self.checkValid(x, y):
            x = int(input("Select an x coordinate: "))
            y = int(input("Select a y coordinate: "))
        while True:
            if self.boardStack[self.convertCoords(x,y)] == "B":
                random.shuffle(self.boardStack)
                continue
            else:
                break
                

    def flag(self, x, y):
        selected = self.convertCoords(x, y)
        if type(self.playerStack[selected]) == int or self.playerStack[selected] == 'F':
            print("This position has already been revealed")
            return
        self.playerStack[selected] = 'F'

    def unflag(self, x, y):
        selected = self.convertCoords(x, y)
        if type(self.playerStack[selected]) == int:
            print("This position has already been revealed")
            return
        self.playerStack[selected] = 'x'

    def checkStatus(self):
        if self.status == '':
            return "In Progress"
        elif self.status == True:
            return "Win"
        else:
            return "Lose"
            

    def _getSolution(self):
        print("== SOLUTION ==")
        print(" ", end="|  ")
        for i in range(1, self.col+1):
            print(i, end="  |  ")
        print("\n-")
        for j in range(1, self.row+1):
            print(j, end="   ")
            split = self.split(self.boardStack,self.col)
            for row in range(self.col):
                print(split[j-1][row], end="     ")
            print ("\n-")

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
        for y in checky:
            for x in checkx:
                if x < 0 or y < 0 or x >= self.col or y >= self.row:

                    continue
                else:
                    if board[y][x] == 'B':
                        bombs += 1
        return bombs

    def showSurround(self, x, y):
        toCheck = []
        x -= 1
        y -= 1
        board = self.split(self.boardStack,self.col)
        # y tells us which list to choose from then x tells us which element within that list we are checking
        checky = [y, y + 1, y - 1]
        checkx = [x , x + 1, x - 1]
        for y in checky:
            for x in checkx:
                if x < 0 or y < 0 or x >= self.col or y >= self.row:
                    # out of range error messes up the check
                    continue
                else:
                    pair = []
                    pair.append(x+1)
                    pair.append(y+1)
                    toCheck.append(pair)
        toShow = []
        for i in toCheck:
            selected = self.convertCoords(i[0],i[1])
        
            if self.checkSurround(i[0],i[1]) == 0:
                toShow.append([i[0],i[1]])
            
            self.playerStack[selected] = self.checkSurround(i[0], i[1])
        return toShow

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




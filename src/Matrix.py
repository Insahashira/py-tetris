class Matrix:

    array = [[]]
    subArray = [[]]
    lineCount = 0

    def __init__(self):
        self.array = [[" ." for _ in range(10)] for _ in range(20)]
        self.subArray = [[" ." for _ in range(10)] for _ in range(3)]
        self.lineCount = 0


    def arraySelector(self, positionY, positionX, val = None): #to access array and subArray more easily
        if val is None:
            if positionY < 0:
                return self.subArray[positionY+3][positionX]
            else:
                return self.array[positionY][positionX]

        elif positionY < 0:
            self.subArray[positionY+3][positionX] = val
        else:
            self.array[positionY][positionX] = val
        return


    def add(self, block, positionX, positionY): #set the array to occupied
        l = len(block.array())
        for i in range(l):
            for j in range(l):
                if block.array()[i][j] == "[]":
                    self.arraySelector(positionY + i, j + positionX, "[]")


    def delete(self, block, positionX, positionY): #set occupied array to blank
        l = len(block.array())
        for i in range(l):
            for j in range(l):
                if block.array()[i][j] == "[]":
                    self.arraySelector(positionY + i, positionX + j, "  ")


    def update(self): #updates the matrix while checking whether the line is full and converts to string
        self.lineChecker()
        self.display()


    def lineChecker(self): #checks if the line is full and delete it
        global lineCount

        for i in range(20):
            count = 0
            for j in range(10):
                if self.array[i][j] == "[]":
                    count += 1
            if count == 10:
                self.lineCount += 1
                self.arrayShifter(i)


    def arrayShifter(self, row): #moves all the lines 1 below after the line gets deleted
        temp = ["  " for _ in range(10)]
        for i in range(row, 0, -1):
            for j in range(10):
                temp[j] = self.array[i-1][j]
                self.array[i][j] = temp[j]
        for i in range(2, 0, -1):
            for j in range(10):
                if i == 0:
                    temp[j] = self.array[0][j]
                else:
                    temp[j] = self.subArray[i-1][j]
                self.subArray[i][j] = temp[j]


    def display(self): #converts the current matrix into string for displaying // outdated
        result = ""
        for i in range(3):
            result += "|"
            for j in range(10):
                result += str(self.subArray[i][j])
                if j != 9:
                    result += "."
                else:
                    result += "|"
            result += "\n"
        result += "|-----------------------------|\n"
        for i in range(20):
            result += "|"
            for j in range(10):
                result += str(self.array[i][j])
                if j != 9:
                    result += "."
                else:
                    result += "|"
            result += "\n"
        result += "===============================\n"
        return result

    def getLineCount(self):
        return str(self.lineCount)
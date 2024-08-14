array = [["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "]]

def add(block, positionX, positionY):
    l = len(block)
    for i in range(l):
        for j in range(l):
            if block[i][j] == "[]":
                if availabilityChecker(positionY, positionX):
                    array[i+positionY][j+positionX] = "[]"

def availabilityChecker(positionY, positionX):
    if array[positionY][positionX] == "  ":
        return True
    else:
        return False

def delete(block, positionX, positionY):
    l = len(block)
    for i in range(l):
        for j in range(l):
            if block[i][j] == "[]":
                array[i+positionY][j+positionX] = "  "


def update(): #updates the matrix while checking whether the line is full and converts to string
    lineChecker()
    display()

def lineChecker(): #checks if the line is full and delete it
    for i in range(20):
        count = 0
        for j in range(10):
            if array[i][j] == "[]":
                count += 1
        if count == 10:
            arrayShifter(i)

def arrayShifter(row): #moves all the lines 1 below after the line gets deleted
    temp = ["  " for _ in range(10)]
    for i in range(row, -1, -1):
        for j in range(10):
            temp[j] = array[i-1][j]
            array[i][j] = temp[j]

def printer():#for terminal debug
    for i in range(20):
        print(array[i])
    print("------------------------------")

def display(): #converts the current matrix into string for displaying
    result = ""
    for i in range(20):
        for j in range(10):
            result += str(array[i][j])
            if j != 9:
                result += "."
        result += "\n"
    return result
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

subArray = [["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
        ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
        ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "]]

def arraySelector(positionY, positionX): #to access array and subArray more easily
    if positionY < 0:
        return subArray[-positionY+1][positionX]
    else:
        return array[positionY][positionX]

def add(block, positionX, positionY):
    l = len(block)
    for i in range(l-1, -1, -1):
        for j in range(l):
            if block[i][j] == "[]":
                if positionY - i < 0:
                    subArray[positionY - i + 3][j + positionX] = "[]"
                else:
                    array[positionY - i][positionX + j] = "[]"

def delete(block, positionX, positionY):
    l = len(block)
    for i in range(l-1, -1, -1):
        for j in range(l):
            if block[i][j] == "[]":
                # arraySelector(positionY - i,positionX + j) = "  "
                if positionY - i < 0:
                    subArray[positionY - i + 3][j + positionX] = "  "
                else:
                    array[positionY - i][positionX + j] = "  "

def availabilityChecker(positionY, positionX):
    if positionY >= 20:
        return False
    elif arraySelector(positionY,positionX) == "  ":
        return True
    return False

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
    for i in range(row, 0, -1):
        for j in range(10):
            temp[j] = array[i-1][j]
            array[i][j] = temp[j]
    for i in range(2, -1, -1):
        for j in range(10):
            if i == 0:
                temp[j] = array[0][j]
            else:
                temp[j] = subArray[i-1][j]
            subArray[i][j] = temp[j]

def printer(): #for terminal debug
    for i in range(20):
        print(array[i])
    print("------------------------------")

def display(): #converts the current matrix into string for displaying
    result = ""
    for i in range(3):
        for j in range(10):
            result += str(subArray[i][j])
            if j != 9:
                result += "."
        result += "\n"
    result += "------------------------------\n"
    for i in range(20):
        for j in range(10):
            result += str(array[i][j])
            if j != 9:
                result += "."
        result += "\n"

    return result
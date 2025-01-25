import copy
import Matrix
import Blocks
import random
import time


posX, posY, block = 0, 0, Blocks.Blocks(None, None, None)
prevBlock, selected, selectedCount = -1, [False for _ in range(7)], 0
queue = []
savedQueue, prevQueue = [], []
matrix = Matrix.Matrix() #matrix for displaying (including the current manipulated block)


def block_selector(): #select the blocks to spawn. If same block is spawned in a row, select to block again
    global block, prevBlock, selected, selectedCount

    if selectedCount == 7:
        selected = [False for _ in range(7)]
        selectedCount = 0

    blocks = [Blocks.TBlock(), Blocks.JBlock(), Blocks.LBlock(), Blocks.IBlock(), Blocks.SBlock(), Blocks.ZBlock(),
              Blocks.SqBlock()]
    blockIdx = random.randrange(0, 7)

    if selected[blockIdx]:
        return block_selector()

    selected[blockIdx] = True
    selectedCount += 1

    block = blocks[blockIdx]

    return block


def spawn(block): #spawn the block and mark it on matrixForDisplay
    global posX, posY
    l = block.size()
    posX = 6 - l
    posY = 1 - l

    # todo: future code for game over
    # for i in range(l):
    #     for j in range(l):
    #         if block.array()[i][j] == "[]" and matrixPlaced[posY + i][posX + j]:
    #             return Something

    # matrix.add(block, posX, posY)


def spawner():
    global block
    while len(queue) < 4:
        temp = block_selector()
        queue.append(temp)

    block = queue.pop(0)
    spawn(block)


def left_margin_cal():
    return marginCal(0)


def right_margin_cal():
    return marginCal(1)


def down_margin_cal():
    return marginCal(2)


def marginCal(type):
    l = block.size()
    arr = block.array()

    for i in range(l):
        for j in range(l):
            if type == 0:
                if arr[j][i] == "[]":  #goes left vertical
                    return i

            elif type == 1:
                if arr[j][l - i - 1] == "[]":  #goes right horizontal
                    return l - i - 1

            elif type == 2:
                if arr[l - i - 1][j] == "[]":  #goes down vertical
                    return l - i - 1

# outdated function
def depthMeasure(): #check availability for downside, how much the actual block is above the level -1 is none
    global block

    l = block.size()
    arr = block.array()
    depth = [-1 for _ in range(l)]
    for i in range(l):
        for j in range(l):
            if arr[j][i] == "[]":
                depth[i] = j
                break

    return depth


def moveLeft():
    global posX, posY
    posXLimit = left_margin_cal()

    if posX + posXLimit > 0 and validityChecker(posX-1, posY, block):
        posX -= 1

def moveRight():
    global posX, posY
    posXLimit = right_margin_cal()

    if posX + posXLimit < 9 and validityChecker(posX+1, posY, block):
        posX += 1


def moveDown():
    global posX, posY, block

    if not validityChecker(posX, posY + 1, block):
        matrix.add(block, posX, posY)
        matrix.lineChecker()
        spawner()

    else:
        posY += 1


def rotateLeft():
    rotateHelper(0)


def rotateRight():
    rotateHelper(1)


def flip():
    rotateHelper(2)


def rotateHelper(type):
    global posX, posY, block

    temp = copy.deepcopy(block)

    if type == 0:
        temp.rotateLeft()
    elif type == 1:
        temp.rotateRight()
    else:
        temp.flip()

    if not validityChecker(posX, posY, temp):
        block_shifter(temp)
        return

    block = temp

def drop():
    global posX, posY, block
    tempY = posY

    while validityChecker(posX, tempY, block):
        tempY += 1

    tempY -= 1
    posY = tempY
    matrix.add(block, posX, posY)
    matrix.lineChecker()
    spawner()

def validityChecker(x, y, blk): #checks whether the block can exist in certain position
    l = blk.size()

    if y >= 20:
        return False

    for i in range(l):
        for j in range(l):
            if y + i > 19 and blk.array()[i][j] == "[]":
                return False

            elif x + j < 0 or x + j > 9:
                if blk.array()[i][j] == "[]":
                    return False

                continue

            elif blk.array()[i][j] == "[]" and matrix.arraySelector(y + i, x + j) == "[]":
                return False

    return True


def block_shifter(temp):
    global posX, posY, block
    l = temp.size()

    if posX < 0:
        for l in range(block.size()):
            if validityChecker(posX + l, posY, temp):
                posX += l
                block = temp
                return

    elif posX + l > 9:
        for l in range(block.size()):
            if validityChecker(posX - l, posY, temp):
                posX -= l
                block = temp
                return


def display(): #converts the current matrix into string for displaying
    result = ""
    for i in range(3):
        result += "|"
        for j in range(10):

            if posX <= j < posX + block.size() and posY <= i - 3 < posY + block.size() and block.array()[i - posY - 3][j - posX] == "[]":
                result += block.array()[i - posY - 3][j - posX]
            else:
                result += matrix.subArray[i][j]

            if j == 9:
                result += "|"

        result += "\n"
    result += "|--------------------|\n"
    for i in range(20):
        result += "|"
        for j in range(10):

            if posX <= j < posX + block.size() and posY <= i < posY + block.size() and block.array()[i - posY][j - posX] == "[]":
                result += "[]"
            else:
                result += matrix.array[i][j]

            if j == 9:
                result += "|"

        result += "\n"
    result += "======================\n"
    return result


def next_screen_display():
    result = "---------\nN E X T\n---------\n"


    for q in queue:
        if len(q.array()) == 2:
            result += "\n"
        for i in range(len(q.array())):
            for j in range(len(q.array())):
                result += q.array()[i][j]
            result += "\n"
        if len(q.array()) != 4:
            result += "\n"

    result += "\n"

    return result


def aux_screen_display():
    result = "---------\nT E S T\n---------\n"
    result += "Lines: " + matrix.getLineCount() + "\n"
    result += "Time: " + "{:.2f}".format(time.time())

    return result


def save_block():
    global block

    if len(prevQueue) > 1:
        if prevQueue[0] == block:
            return

    prevQueue.append(block)
    if len(savedQueue) == 0:
        savedQueue.append(block)
        spawner()

    else:
        savedQueue.append(block)
        block = savedQueue.pop(0)
        spawn(block)

    if len(prevQueue) > 2:
        prevQueue.pop(0)


start = 0

def time_start():
    global start
    start = time.time()

def time_measure():
    if time.time() - start > 1:
        moveDown()
        time_start()
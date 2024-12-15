import copy
import Matrix
import Blocks
import random


posX, posY, block, prevBlock = 0, 0, Blocks.Blocks(None, None), -1
matrixPlaced = Matrix.Matrix() #matrix to record already placed blocks
matrixForDisplay = Matrix.Matrix() #matrix for displaying (including the current manipulated block)


def blockSelector(): #select the blocks to spawn. If same block is spawned in a row, select to block again
    global block, prevBlock

    blocks = [Blocks.TBlock(), Blocks.JBlock(), Blocks.LBlock(), Blocks.IBlock(), Blocks.SBlock(), Blocks.ZBlock(),
              Blocks.SqBlock()]
    blockIdx = random.randrange(0, 7)
    block = blocks[blockIdx]

    if prevBlock != -1:
        if blockIdx == prevBlock:
            return blockSelector()

    prevBlock = blockIdx
    return block


def leftMarginCal():
    return marginCal(0)


def rightMarginCal():
    return marginCal(1)


def downMarginCal():
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

    matrixForDisplay.add(block.array(), posX, posY)


def moveLeft():
    global posX, posY
    posXLimit = leftMarginCal()

    if posX + posXLimit > 0 and validityChecker(posX-1, posY, block):
        matrixForDisplay.delete(block.array(), posX, posY)
        posX -= 1
        matrixForDisplay.add(block.array(), posX, posY)


def moveRight():
    global posX, posY
    posXLimit = rightMarginCal()

    if posX + posXLimit < 9 and validityChecker(posX+1, posY, block):
        matrixForDisplay.delete(block.array(), posX, posY)
        posX += 1
        matrixForDisplay.add(block.array(), posX, posY)


def moveDown():
    global posX, posY, block

    if not validityChecker(posX, posY + 1, block):
        matrixPlaced.add(block.array(), posX, posY)
        matrixPlaced.lineChecker()
        matrixForDisplay.lineChecker()
        spawn(blockSelector())
        return

    matrixForDisplay.delete(block.array(), posX, posY)
    posY += 1
    matrixForDisplay.add(block.array(), posX, posY)


def rotateLeft():
    global posX, posY, block

    temp = copy.deepcopy(block)
    temp.rotateLeft()

    if not validityChecker(posX, posY, temp):
        blockShifter(temp)
        return

    matrixForDisplay.delete(block.array(), posX, posY)
    block = temp
    matrixForDisplay.add(block.array(), posX, posY)


def rotateRight():
    global posX, posY, block

    temp = copy.deepcopy(block)
    temp.rotateRight()

    if not validityChecker(posX, posY, temp):
        blockShifter(temp)
        return

    matrixForDisplay.delete(block.array(), posX, posY)
    block = temp
    matrixForDisplay.add(block.array(), posX, posY)


def validityChecker(x, y, blk): #checks whether the block can exist in certain position
    l = blk.size()

    if y >= 20:
        return False

    for i in range(l):
        for j in range(l):
            if y + i > 19:
                if blk.array()[i][j] == "[]":
                    return False

                continue

            elif x + j < 0 or x + j > 9:
                if blk.array()[i][j] == "[]":
                    return False

                continue

            elif blk.array()[i][j] == "[]" and matrixPlaced.arraySelector(y + i, x + j) == "[]":
                return False

    return True


def blockShifter(temp):
    global posX, posY, block
    l = temp.size()

    if posX < 0:
        for l in range(block.size()):
            if validityChecker(posX + l, posY, temp):
                matrixForDisplay.delete(block.array(), posX, posY)
                posX = posX + l
                block = temp
                matrixForDisplay.add(block.array(), posX, posY)
                return

    elif posX + l > 9:
        for l in range(block.size()):
            if validityChecker(posX - l, posY, temp):
                matrixForDisplay.delete(block.array(), posX, posY)
                posX = posX - l
                block = temp
                matrixForDisplay.add(block.array(), posX, posY)
                return
import Matrix
import Blocks
import random

posX = 0
posY = 0
block = ""

def blockSelector():
    global block
    blocks = [Blocks.TBlock(), Blocks.JBlock(), Blocks.LBlock(), Blocks.IBlock(), Blocks.SBlock(), Blocks.ZBlock(), Blocks.SqBlock()]
    block = blocks[random.randrange(0,7)]
    return block

def marginCal(type):
    l = block.size()
    arr = block.array()
    for i in range(l):
        for j in range(l):
            if type == 0:
                if arr[j][i] == "[]": #goes left vertical
                    return i
            elif type == 1:
                if arr[j][l-i-1] == "[]": #goes right horizontal
                    return l-i-1         
            elif type == 2:
                if arr[l-i-1][j] == "[]": #goes down vertical
                    return l-i-1
                
def depthMeasure(): #rn for down side
    l = block.size()
    arr = block.array()
    depth = [-1 for _ in range(l)]
    for i in range(l):
        for j in range(l):
            if arr[l-j-1][i] == "[]":
                depth[i] = l-j-1
                break
    return depth
    
def bottomDetector():
    l = block.size()
    depth = depthMeasure()
    for i in range(l):
        if Matrix.availabilityChecker(posY + depth[i]+1, posX + i):
           pass
        else:
            return True 
    return False

def spawn(block):
    global posX
    global posY
    l = block.size()
    posX = 5-l
    posY = 0
    Matrix.add(block.array(), posX, posY)

def moveLeft():
    global posX
    global posY
    posXLimit = marginCal(0)
    if posX + posXLimit > 0:
        Matrix.delete(block.array(), posX, posY)
        posX -= 1
        Matrix.add(block.array(), posX, posY)

def moveRight():
    global posX
    global posY
    posXLimit = marginCal(1)
    print(posXLimit)
    if posX + posXLimit < 9:
        Matrix.delete(block.array(), posX, posY)
        posX += 1
        Matrix.add(block.array(), posX, posY)

def moveDown():
    global posX
    global posY
    posYLimit = marginCal(2)
    if bottomDetector():
        spawn(blockSelector())
    elif posY + posYLimit < 19:
        Matrix.delete(block.array(), posX, posY)
        posY += 1
        Matrix.add(block.array(), posX, posY)

def rotateLeft():
    global posX
    global posY
    temp = block.array()
    Matrix.delete(block.array(), posX, posY)
    block.rotateLeft()
    Matrix.add(block.array(), posX, posY)

def rotateRight():
    global posX
    global posY
    Matrix.delete(block.array(), posX, posY)
    block.rotateRight()
    Matrix.add(block.array(), posX, posY)
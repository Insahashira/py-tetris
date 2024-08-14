import Matrix
import Blocks
# import time
# import Tkinter
import random

posX = 0
posY = 0
block = ""

def blockSelector():
    global block
    blocks = [Blocks.TBlock(), Blocks.JBlock(), Blocks.LBlock(), Blocks.IBlock(), Blocks.SBlock(), Blocks.ZBlock(), Blocks.SqBlock()]
    block = blocks[random.randrange(0,7)]
    return block

def spawn(block):
    global posX
    global posY
    posX = 5
    posY = 0
    Matrix.add(block.array(), posX, posY)

def moveLeft():
    global posX
    global posY
    Matrix.delete(block.array(), posX, posY)
    posX -= 1
    Matrix.add(block.array(), posX, posY)

def moveRight():
    global posX
    global posY
    Matrix.delete(block.array(), posX, posY)
    posX += 1
    Matrix.add(block.array(), posX, posY)

def moveDown():
    global posX
    global posY
    Matrix.delete(block.array(), posX, posY)
    posY += 1
    Matrix.add(block.array(), posX, posY)
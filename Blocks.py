import abc
class Blocks(metaclass=abc.ABCMeta):

    def __init__(self, type, arr):
        self.arr = arr
        self.type = type
    
    position = 0

    def rotateLeft(self):
        if(self.type == 0):
            self.rotatorL()
        elif(self.type == 1):
            self.rotator()
        else:
            pass
        
    def rotateRight(self):
        if(self.type == 0):
            self.rotatorR()
        elif(self.type == 1):
            self.rotator()
        else: 
            pass

    def flip(self):
        if(type == 0):
            self.rotatorL()
            self.rotatorL()
    
    def rotator(self):
        if(self.position == 0):
            self.rotatorR()
            self.position = 1
        else:
            self.rotatorL()
            self.position = 0

    def rotatorL(self):
        l = len(self.arr)
        temp = [["   " for _ in range(l)] for _ in range(l)]
        for i in range(l):
            for j in range(l):
                temp[l-j-1][i] = self.arr[i][j]
        self.arr = temp

    def rotatorR(self):
        l = len(self.arr)
        temp = [["   " for _ in range(l)] for _ in range(l)]
        for i in range(l):
            for j in range(l):
                temp[j][l-i-1] = self.arr[i][j]
        self.arr = temp

    def size(self):
        return len(self.arr)
    
    def array(self):
        return self.arr

class TBlock(Blocks):
    def __init__(self):
        super().__init__(0, [["   ", "[]", "   "],["[]","[]","[]"],["   ","   ","   "]])

class JBlock(Blocks):
    def __init__(self):
        super().__init__(0, [["   ", "[]", "   "],["   ","[]","   "],["[]","[]","   "]])

class LBlock(Blocks):
    def __init__(self):
        super().__init__(0, [["   ", "[]", "   "],["   ","[]","   "],["   ","[]","[]"]])

class IBlock(Blocks):
    def __init__(self):
        super().__init__(1, [["   ", "   ", "   ", "[]"],["   ", "   ", "   ", "[]"],["   ", "   ", "   ", "[]"], ["   ", "   ", "   ", "[]"]])

class SBlock(Blocks):
    def __init__(self):
        super().__init__(1, [["   ", "[]", "   "],["   ","[]","[]"],["   ","   ","[]"]])

class ZBlock(Blocks):
    def __init__(self):
        super().__init__(1, [["   ", "[]", "   "],["[]","[]","   "],["[]","   ","   "]])

class SqBlock(Blocks):
    def __init__(self):
        super().__init__(2, [["[]", "[]"],["[]", "[]"]])

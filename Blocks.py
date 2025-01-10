import abc


class Blocks(metaclass=abc.ABCMeta):
    position = 0

    def __init__(self, type, arr, shape):
        self.arr = arr
        self.type = type
        self.shape = shape

    def rotateLeft(self):
        if self.type == 0:
            self.rotatorL()

        elif self.type == 1:
            self.rotator()

        else:
            pass

    def rotateRight(self):
        if self.type == 0:
            self.rotatorR()

        elif self.type == 1:
            self.rotator()

        else:
            pass

    def flip(self):
        if self.type == 0:
            self.rotatorL()
            self.rotatorL()

    def rotator(self):
        if self.position == 0:
            self.rotatorR()
            self.position = 1

        else:
            self.rotatorL()
            self.position = 0

    def rotatorL(self):
        l = len(self.arr)
        temp = [["  " for _ in range(l)] for _ in range(l)]

        for i in range(l):
            for j in range(l):
                temp[l - j - 1][i] = self.arr[i][j]

        self.arr = temp

    def rotatorR(self):
        l = len(self.arr)
        temp = [["  " for _ in range(l)] for _ in range(l)]

        for i in range(l):
            for j in range(l):
                temp[j][l - i - 1] = self.arr[i][j]

        self.arr = temp

    def size(self):
        return len(self.arr)

    def array(self):
        return self.arr

    def __eq__(self, other):
        return self.shape == other


class TBlock(Blocks):
    def __init__(self):
        super().__init__(0, [["  ", "[]", "  "], ["[]", "[]", "[]"], ["  ", "  ", "  "]], "T")


class JBlock(Blocks):
    def __init__(self):
        super().__init__(0, [["  ", "[]", "  "], ["  ", "[]", "  "], ["[]", "[]", "  "]], "J")


class LBlock(Blocks):
    def __init__(self):
        super().__init__(0, [["  ", "[]", "  "], ["  ", "[]", "  "], ["  ", "[]", "[]"]], "L")


class IBlock(Blocks):
    def __init__(self):
        super().__init__(1, [["  ", "  ", "  ", "[]"], ["  ", "  ", "  ", "[]"], ["  ", "  ", "  ", "[]"],
                             ["  ", "  ", "  ", "[]"]], "I")


class SBlock(Blocks):
    def __init__(self):
        super().__init__(1, [["  ", "[]", "  "], ["  ", "[]", "[]"], ["  ", "  ", "[]"]], "S")


class ZBlock(Blocks):
    def __init__(self):
        super().__init__(1, [["  ", "[]", "  "], ["[]", "[]", "  "], ["[]", "  ", "  "]], "Z")


class SqBlock(Blocks):
    def __init__(self):
        super().__init__(2, [["[]", "[]"], ["[]", "[]"]], "Sq")

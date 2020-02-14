import copy

class Array2d:
    def __init__(self, w, h, v, r = (0,19)):
        self.w = w
        self.h = h
        self.v = []
        
        
        if v >= 0:
            temp = []
            for y in range(h):
                temp.append(v)
            for x in range(w):
                self.v.append(copy.deepcopy(temp))
        if v < 0:
            for x in range(w):
                temp = []
                for y in range(h):
                    t = random.randint(r[0],r[1])
                    temp.append(t)
                self.v.append(copy.deepcopy(temp))
                    
    def addrow(self, v):
        self.h += 1
        for x in range(self.w):
            self.v[x].append(v)
    def subrow(self):
        if self.h > 1:
            self.h -= 1
            for x in range(self.w):
                self.v[x].pop()
    def addcol(self, v):
        temp = []
        self.w += 1
        for y in range(self.h):
            temp.append(v)
        self.v.append(copy.deepcopy(temp))
    def subcol(self):
        if self.w > 1:
            self.w -= 1
            self.v.pop()

    def setv(self, x, y, v):
        self.v[x][y] = v

    def getv(self, x, y):
        return self.v[x][y]

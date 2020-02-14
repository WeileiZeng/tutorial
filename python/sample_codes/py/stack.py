class Stack():
    def __init__(self):
        self.stack=[]
    def append(self,x):
        self.stack.append(x)
    def pop(self):
        a=len(self.stack)
        if a>0:
            return self.stack.pop()
        else:
            return 0    

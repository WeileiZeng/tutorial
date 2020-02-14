import string

class Set():
    def __init__(self,elements=None):
        self.Set={}
        if elements !=None:
            ee=str.split(elements,',')
            for i in ee:
                self.Set[i]=i
            self.elements=self.Set.keys()
    def addElement(self,x):
        self.Set[x]=x
    def deleteElement(self,x):
        del self.Set[x]
    def menber(self,x):
        if x in self.Set:
            print 'True'
            return True
        else:
            print 'False'
            return False
    def intersection(self,set2):
        ee=Set()
        for i in self.Set:
            if i in set2.Set:
                ee.addElement(i)
        print ee.Set
        return ee
    def union(self,set2):
        ee=Set()
        for i in self.Set:
            ee.addElement(i)
        for i in set2.Set:
            ee.addElement(i)
        print ee.Set
        return ee
    def subtract(self,set2):
        ee=Set()
        for i in self.Set:
            if i not in set2.Set:
                ee.addElement(i)
        print ee.Set
        return ee
    def __str__(self):# why this doesn't work?
        return self.Set
    
def test():
    y=Set('a,s,d,f,g,h')
    x=Set('a,s,d,z,x,c,v')
    print x
    z=y.union(x)
    c=y.intersection(x)
    v=y.subtract(x)
    
    
if __name__ == "__main__":
    test()
        

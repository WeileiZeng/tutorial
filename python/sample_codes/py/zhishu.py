def main1():
        s=0
        x=input("enter an integer: ")
        if x>99999999:
                print 'the number is too big to calculate'
        elif x in [1,2,3]:
                print 'Ture'
                return True
        else:
                for i in range(x-2):
                        a=x%(i+2)
                        if a == 0:
                                print i+2
                                print 'False'
                                return False
                                break
                if a>0:
                        print 'False'
                        return False
        

def main():
        for i in range(100):
                main1()
                y=raw_input('press \'enter\' to retry or n...')
                if y=='n':
                        break
def main2(x):


        if x in [1,2,3]:
                print x

                return True
        else:
                for i in range(x-2):
                        a=x%(i+2)
                        if a == 0:
                
                     
                                return False
                                break

                print x
                return True
def main3():
        i=1
        while True:
                
                main2(i)
                i+=1


main3()
        
                        
                        

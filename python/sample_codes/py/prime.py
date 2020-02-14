def main1():
    n=input('enter an interger: ')
    b1={}
    for i in range(2,n+1):
        b1[i]=i
    for i in range(2,n+1):
        b2=b1.copy()
        if i in b1:
            for j in b1:
                if j>i and j%i==0:
                    del b2[j]
        b1=b2
    bb=[]
    for i in b1:
        bb.append(i)
    q=0
    while q==0:
        q=1
        for i in range(len(bb)-1):
            a=bb[i]
            b=bb[i+1]
            if a>b:
                bb[i]=b
                bb[i+1]=a
                q=0
    print bb
    return bb
def main():
        for i in range(100):
                main1()
                y=raw_input('press \'enter\' to retry or n...')
                if y=='n':
                        break

main()
        
                        
                        

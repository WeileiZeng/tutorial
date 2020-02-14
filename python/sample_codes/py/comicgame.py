#this module canot find the answer to the game because of too much cases
"""The aim of this online puzzle is to convert all of the White pieces on
the game board to Black pieces. Clicking on a piece with the mouse
will change it from White to Black, and vice- versa. It will also
reverse the colors of all horizontally and vertically adjace nt
pieces. You can select the size of the board - from 3x3 to 8x8. The
Moves counter will turn red to indicate the minimum number of moves
necessary to win, for the selected board size. Beyond the minimum
number of moves, the Moves counter will turn gray."""
import copy
def printArray(array):
    for lists in array:
        print lists
def main():
    n=5
    numberOfAnswer=0
    array1=[]
    for i in range(n):
        cc=[]
        for i in range(n):
            cc.append(0)
        array1.append(cc)
    array1[n-1][n-1]=-1
    q=0
    while q<1000:
        array1[n-1][n-1]=array1[n-1][n-1]+1
        q=0
        for j in range(n):
            for k in range(n):
                if array1[n-j-1][n-1-k]==2:
                    array1[n-j-1][n-k-1]=0
                    if k==9:
                        array1[n-j-2][9]=array1[n-j-2][9]+1
                    else:
                        array1[n-j-1][n-k-2]=array1[n-j-1][n-k-2]+1
                else:
                    q=1
                    break
            if q==1:
                break
        print_array1(array1)
        array2=[]
        for i in range(n+2):
            cc=[]
            for i in range(n+2):
                   cc.append(0)
            array2.append(cc)
        for j in range(n):
            for k in range(n):
                if array1[j][k]==1:
                    if array2[j+1][k+1]==0:#center
                        array2[j+1][k+1]=1
                    else:
                        array2[j+1][k+1]=0
                    if array2[j+1][k]==0:#left
                        array2[j+1][k]=1
                    else:
                        array2[j+1][k]=0
                    if array2[j+1][k+2]==0:#right
                        array2[j+1][k+2]=1
                    else:
                        array2[j+1][k+2]=0
                    if array2[j][k+1]==0:#up
                        array2[j][k+1]=1
                    else:
                        array2[j][k+1]=0
                    if array2[j+2][k+1]==0:#down
                        array2[j+2][k+1]=1
                    else:
                        array2[j+2][k+1]=0
        del array2[n+1]
        del array2[0]
        for i in range(n):
            del array2[i][n+1]
            del array2[i][0]
        s=0
        for i in range(n):
            for j in range(n):
                if array2[i][j]==0:
                    s=s+1
                    break
            if s>0:
                break
        if s==0:
            q=q+1
            print q
            for i in range(n):
                print array2[i]
        print numberOfAnswer
        numberOfAnswer=numberOfAnswer+1
def main2(n):
    numberOfAnswer=1
    i=-1
    maximum=2**(n*n)-1
    while i <maximum:
        i+=1
        array1=bin(i)#array1 is a string of a number expressed in binary system
                     #the 1 and 0 stand for whether a position is pressed or not
        array1='0'*(n*n+2-len(array1))+array1[2:] #ensure that array is enough long
        #print array1
        array2=[] #to check the answer
        for x in range(n+2):#create an array (n+2)*(n+2)
            cc=[]
            for y in range(n+2):
                   cc.append(0)
            array2.append(cc)
        for j in range(n):
            for k in range(n):
                if array1[j*n+k]=='1':
                    array2[j+1][k+1]+=1   #center
                    array2[j+1][k]+=1     #left
                    array2[j+1][k+2]+=1   #right
                    array2[j][k+1]+=1     #up
                    array2[j+2][k+1]+=1   #down
        s=0
        for i in range(n):
            for j in range(n):
                if array2[i+1][j+1]%2==0:
                    s=s+1
                    break
            if s>0:
                break
        if s==0:
            for i in range(n):
                
                print array1[n*i:n*i+n]
            printArray(array2)
            print "numberOfAnswer is ", numberOfAnswer
            numberOfAnswer += 1
main2(6)

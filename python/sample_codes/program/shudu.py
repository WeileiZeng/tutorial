#shudu.py
import copy

a=[[0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0]]
b=[[8,0,0,0,0,0,0,0,0],
   [0,0,3,6,0,0,0,0,0],
   [0,7,0,0,9,0,2,0,0],
   [0,5,0,0,0,7,0,0,0],
   [0,0,0,0,4,5,7,0,0],
   [0,0,0,1,0,0,0,3,0],
   [0,0,1,0,0,0,0,6,8],
   [0,0,8,5,0,0,0,1,0],
   [0,9,0,0,0,0,4,0,0]]
c=[[1,4,0,5,0,0,0,8,0],
   [0,7,2,0,0,0,0,0,0],
   [0,0,0,2,6,0,1,0,4],
   [0,0,8,0,0,0,0,0,7],
   [0,0,0,0,0,3,0,2,0],
   [4,0,0,0,0,1,0,0,0],
   [0,0,0,0,0,0,9,0,8],
   [9,0,0,0,2,0,5,4,0],
   [0,5,7,9,4,0,0,0,0]]
err=".......111111111....111111........11111.....11111....111111.........\n.......1............11....11.....11...11...11...11...11...11........\n.......1............11.....11....11...11...11...11...11....11.......\n.......1............11....11.....11...11...11...11...11...11........\n.......111111111....1111111......11...11...11...11...111111.........\n.......1............1111.........11...11...11...11...1111...........\n.......1............11..11.......11...11...11...11...11..11.........\n.......1............11...11......11...11...11...11...11...11........\n.......111111111....11.....11.....11111.....11111....11.....11......"
def print_arrow(arrow):
    print "the arrow you want to print is..."
    for line in arrow:
        print line
def check_position_row(arrow,row,number):
    for i in range(9):
        if arrow[i][row-1]==number:#the number has been used in the row
            return 1
    return 0 #the number doesn't have been used in the row

def check_position_square(arrow,square,number):
    #square is a list represent its position, eg: [2,1]means line 2nd, row 1st
    #print "square=",square
    for i in range(3):
        #print "number=",number
        #print "part of number in the square...",arrow[square[0]*3-i-1][(square[1]*3-3):(square[1]*3)]
        if number in arrow[square[0]*3-i-1][(square[1]*3-3):(square[1]*3)]:
            return 1
    return 0 #the number doesn't have been used in the row



def check_position(arrow,line,number):
    #check which positons in the line the number can be located in
    positions=[]
    for i in range(9):#the line doesnot have the number
        if arrow[line-1][i]==number:
            return positions
    for i in range(9):
        #print "present position checked...",[line,i+1]
        if arrow[line-1][i]==0:#the position is empty
            if check_position_row(arrow,i+1,number)==0:#the row doesnot have the number
                if check_position_square(arrow,[(line-1)/3+1,i/3+1],number)==0:#the square doesnot have the number
                    positions.append(i+1)
    #print "line,positions= ",line,positions
    return positions #positions is a list including the possible positions in the line the number can be in          
    # if positions is a empty list, it means there has been some error
            
def check_position2(arrow,line,number):
    #print "line=...",line
    if line>9:
        print "arrow="
        print_arrow(arrow)
        print "change number: ",number+1,"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
        if number > 9:
            print "arrow="
            print_arrow(arrow)
            return
        else:
            arrow2=copy.deepcopy(arrow)
            check_position2(arrow2,1,number+1)
    else:
        positions=check_position(arrow,line,number)
        if positions==[]:
                for i in range(9):#the line does not have the number
                    if number in arrow[line-1]:
                        arrow2=copy.deepcopy(arrow)
                        check_position2(arrow2,line+1,number)
                        
                    else:
                        pass
                        #print "error:  positions is [].............................................................."   
                        
        else:
            
            for n in positions:
                #print "present position trying...",line,n
                arrow2=copy.deepcopy(arrow)
                arrow2[line-1][n-1]=number
                #print_arrow(arrow2)
                check_position2(arrow2,line+1,number)
                

##def check_number(arrow,i):#number i
##    arrow0=arrow
##    arrows=[]
##    if i>9:
##        return arrow
##    else:
##    for j in range(9):# line j
##        positions=check_position(arrow,j,i)
##        if positions==[]:
##            pass
##        else:
##            for n in positions:
##                arrow[j][n-1]=i
def check_line(arrow,line,i):
    pass
def trying(arrow,i):
    if i>9:
        return arrow
    else:
        arrows=check_number(arrow,i)
        check(arrow,i+1)
    
def test():
    #print check_position(b,2,8)
    #print check_position_square(b,[2,2],2)
    check_position2(b,1,1)
test()

# This a program can turn a number round
# reverse.py
def reverse(num,rnum):
    rnum=rnum*10+num%10
    if num>=10:
        num=(num-num%10)/10
        reverse(num,rnum)
    else: print rnum

num=input("Please input an integer:")
reverse(num,0)


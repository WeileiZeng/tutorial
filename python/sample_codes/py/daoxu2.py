
	
def main():
    for i in range(10):
	ss =input("enter a number: ")
# 
	aaa= str(ss)
	a = len(aaa)
	for i in range(a):
		if ss%10 ==0 and a > 0:
			ss = ss/10
		else:
			break
#	
	sss=str(ss)
	ssss=sss[::-1]
	print ssss
	x = input("enter 1 to continue or 0 to end...")
	if x == 0:
		break

main()
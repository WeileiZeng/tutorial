def main():
    for i in range(10):
	ss =input("enter a number: ")
	sss=str(ss)
	ssss=sss[::-1]
	print ssss
	x = input("enter 1 to continue or 0 to end...")
	if x == 0:
		break

main()
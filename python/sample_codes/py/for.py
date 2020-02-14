def main():
	for i in range(10):
		print "the time is: ",i+1
		n = input("enter 1 to continue or 0 to end: ")
		if n >0:
			x,y,z = input("enter x,y,z: ")
			a = (x+y+z+ 0.0 )/3
			print "the average is: ",a

	b = input("enter any integer to end the program:  ")

main()

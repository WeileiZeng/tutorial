# check the date form
def main():
	x,y,z = input("enter a date in the form month , day , year : ")
	mylist = [2,4,6,9,11]
	if x > 12 or x < 1 :
		print "month error"
	elif y>31 or y < 1 :
		print "day error"
	elif x in mylist and y > 30 :
		print "day error"
	else:
		print "you are rignt!"

main()
	

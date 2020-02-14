# this is a program that can changes the points into grades
def main():
	a,b,c,d =89,79,69,59
	x = input("enter your score: ")
	if x > a:
		print "your grade is A"
	elif x > b:
		print "your score is B"
	elif x > c:
		print "your score is C"
	elif x > d:
		print "your score is D"
	else :
		print "your score is F"

main()
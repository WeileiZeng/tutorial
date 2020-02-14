def main():
	x = input("enter a sentence: ")
	import string
	y = string.split(x)
	a = len(y)
	b = len(x)
	c = (b+1.0)/a-1
	print "the average length of words in the sentence is: ",c

main()
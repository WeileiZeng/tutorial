# a program that counts the number of words in a sentence entered by the user
def main():
	import string
	x = input("innput a sentence: ")
	y = string.split(x)
	z = len(y)
	print "the number of words is: ",z

main()
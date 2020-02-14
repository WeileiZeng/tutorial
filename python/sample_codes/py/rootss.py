# qiu er ci fang cheng de gen
import math
def main():
	    a, b, c = input("Enter three coefficients: ")
	    discRoot = math.sqrt(b*b - 4*a*c)
	    r1 = (-b + discRoot) / (2 * a)
	    r2 = (-b - discRoot) / (2 * a)
	    print "The solutions are:", r1, r2

main()


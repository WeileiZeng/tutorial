def fibo(x):
	if x<0:
		print -1
	elif x>1:
		a=0
		b=1
		for i in range(x-2):
			c=a
			a=b
			b=c+b
		print b
	else:
		print x

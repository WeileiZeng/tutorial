#output all sequence cosisting of "A","T","G","E"
def sequence(n):
	base=['A','T','C','G']
	print reduce(lambda x,y:[(a+b) for a in x for b in y],map(lambda x:[x]*n,[base])[0])

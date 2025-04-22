import itertools

print("WARNING, this code will definetely crash your laptop")

for a,b,c in itertools.product(itertools.count(0),xrange(0,10),xrange(0,10)):
	print(a)
	print(b)
	print(c)
	if a > 20: break
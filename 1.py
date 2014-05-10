a = 0 #fib a
b = 1 #fib b
d = 0 #sum
while a+b < 4000000:
	c = a+b	
	if c%2 == 0: #check if c is even
		d += a+b #if so then add to the total
	a = b
	b = c
print (d)

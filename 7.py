'''
What is the 10001th prime number?
'''
def prime(z): #prime checker
  i = 2
  while i < z:
    if z % i == 0:
      return z/i         
    i = i + 1
  return z
def primer(x):
	np = 0 #prime ticker
	tick = 2
	while np != x:
		if prime(tick) == tick: #prime checker
			np += 1
			current = tick #current prime
		tick += 1
	return current 
print (primer(10001))
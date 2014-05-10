'''
What is the largest prime factor of the number 600851475143 ?
'''
def prime(z):
  i = 2
  n = z
  while i * i < n:
    while n % i == 0:
      n = n / i
    i = i + 1
  return n
print (prime(5))
""" 
Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""
import math
s=0
for i in range(101): #square of sum
	s += i
ss = s ** 2

f=0
for i in range(101): #sum of squares
	f += i ** 2
print(ss-f)
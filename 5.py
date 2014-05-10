'''
What is the smallest positive number that is 
evenly divisible by all of the numbers from 1 to 20?
'''
m = 20
ls = [9, 11, 12, 13, 14, 15, 16, 17, 18, 19]
a = m
i = 0
while i < 10:
  if ( a % ls[i]) != 0:
    a += m
    i = 0
    continue
  else:
    i += 1
print (a)
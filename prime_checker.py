#!/bin/python

import math

def primeCheck(number):
 isPrime = False
 for i in range(2, int(math.sqrt(number))):
  if (inp % i == 0):
   isPrime = True
   break
 
 return isPrime
 
inp = int(raw_input('Check prime number: '))
print "Is prime? " + str(primeCheck(inp))

# a somewhat efficient primer checker (checks if a number is prime or not)
# works in O(sqrt(n)) steps

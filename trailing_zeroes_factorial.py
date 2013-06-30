#!/bin/python

import math

def trailingZeroes(number):
  fact = math.factorial(number)
  zeroesCnt = 0
  while (fact % 10 == 0):
    zeroesCnt+=1
    fact /= 10
  return zeroesCnt

def trailingZeroesBetter(number):
  zeroesCnt = 0
  currentFactor = 5
  while (number >= currentFactor):
    zeroesCnt += number / currentFactor
    currentFactor *= 5
  return zeroesCnt
 
input = int(raw_input('Enter a number: '))
print trailingZeroesBetter(input) == trailingZeroes(input)

# trailingZeroesBetter(number) will find the number of trailing zeroes in a factorial efficiently, whereas
# trailingZeroes(number) will just calculate the factorial of the given number and count them manually 
# (unefficently)

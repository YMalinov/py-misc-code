#!/bin/python

def multitorial(number, level):
  if (level == 0):
    return number
    
  result = 1
  for num in range(2, number + 1):
    result *= multitorial(num, level - 1) 
     
  return result

number = int(raw_input('Enter a number: '))
levels = int(raw_input('Enter levels: '))

print multitorial(number, levels)

# we all know the factorial of a number is the product of all numbers from 1 to the number [1 * 2 *...* number = number!]
# the superfactorial of a number is the product of all factorials from 1 to the number [1! * 2! *...* number! = number!!]
# if we call the factorial of a number level 1, and the superfactorial - level 2, this program can calculate the factorial
# to whatever level you give it

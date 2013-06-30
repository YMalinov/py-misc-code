#!/bin/python

inp = int(raw_input('Enter which member: '))
firstNum = 0
secondNum = 1
thirdNum = 1

for i in range(0, inp - 1):
  thirdNum = firstNum + secondNum
  firstNum = secondNum
  secondNum = thirdNum
  
  print str(thirdNum) + ', '
print 'The ' + str(inp) + 'th number of the Fibonacci sequence is ' + str(thirdNum) + '.'

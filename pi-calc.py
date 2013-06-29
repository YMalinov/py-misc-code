from mpmath import *

def calcPi(decimalPlaces):
  setPrecision(decimalPlaces)
  a = mpf(1)
  b = mpf(1.0 / sqrt(2))
  t = mpf(1.0 / 4.0)
  p = mpf(1.0)

  prec = mpf(1.0 / mpf(10**decimalPlaces))
  while (abs(a - b) >= prec):
    aOld = a
    a = (a + b) / 2.0
    b = sqrt(aOld * b)
    t -= p * (aOld - a) ** 2
    p *= 2.0

  dividend = (a + b) ** 2
  divisor = 4 * t
  return dividend / divisor

def setPrecision(decimalPlaces):
  mp.dps = decimalPlaces

n = int(raw_input('Calculate Pi to how many places: '))

print calcPi(n)

# will attempt to calculate Pi to the n-th decimal place, using the famous Gauss-Legendre 
# algorithm. to use this, you'll need the mpmath library for arbitrary-precision arithmetic.
# because of algorithm limitations, the number of the result's decimal places will be the 
# input +/- 1.
# also redirect the output to a file or /dev/null when testing with big numbers, because the
# terminal fills up fairly quickly :)

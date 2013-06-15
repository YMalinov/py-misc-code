def fact(x):
	ans1 = 1
	while x > 1:
		ans1 = ans1 * x
  		x = x - 1
	return ans1 

def revfact(inp):
	if inp == 0: return 1
	if inp == 1: return 1
	if inp == 2: return 2
	if inp == 6: return 3
	if not inp > 0: return 'The number should be positive, not ' + str(inp) + '.' 
	chk = 1
	while inp>=fact(chk):
		if fact(chk) == inp: 
			return chk
		chk += 1
	return str(inp) + ' is not the factorial of any number.'
	
input = int(raw_input('Enter a number: '))
print revfact(input), "!"

# this program finds which number is the input the factorial of (x! = input, x = ?)
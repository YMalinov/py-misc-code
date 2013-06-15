def stringRepeater(char, count):
  result = ""
  for i in range(0, count):
    result += char
  
  return result

def drawTree(size):
  assert size > 0, 'tree size must be positive'
  
  dotCount = size - 2
  starCount = 1
  for i in range(0, size - 1):
    dots = stringRepeater(".", dotCount)
    stars = stringRepeater("*", starCount)
    print dots, stars, dots
  
    dotCount -= 1
    starCount += 2
  
  dots = stringRepeater('.', size - 2)
  print dots, "*", dots

input = int(raw_input('Enter the tree size: '))
drawTree(input)

# a popular Telerik Academy exam prep task
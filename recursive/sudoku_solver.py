import math

def solveSudoku(matrix, row, col):
  if row == len(matrix):
    printMatrix(matrix)
    print ""
    return

  if col == len(matrix):
    return solveSudoku(matrix, row + 1, 0)

  if matrix[row][col] != 0:
    return solveSudoku(matrix, row, col + 1)
  
  for guess in range(1, len(matrix) + 1):
    if isPossibleNumber(matrix , guess, row, col):
      matrix[row][col] = guess
      solveSudoku(matrix, row, col)
      matrix[row][col] = 0

def isPossibleNumber(matrix, number, row, col):
  size = len(matrix)
  for currentCol in range(0, size):
    if matrix[row][currentCol] == number:
      return False
  
  for currentRow in range(0, size):
    if matrix[currentRow][col] == number:
      return False
   
  squareSize = int(math.sqrt(size))
  startingRow = row - (row % squareSize)
  startingCol = col - (col % squareSize)
  
  for curRow in range(startingRow, startingRow + squareSize):
     for curCol in range(startingCol, startingCol + squareSize):
       if matrix[curRow][curCol] == number:
         return False
         
  return True

def printMatrix(matrix):
  for row in range(0, len(matrix)):
    line = ""
    for col in range(0, len(matrix[0])):
      line += str(matrix[row][col]) + " "
    print line
  
  return
  
sudoku = [[0, 0, 7, 0, 0, 1, 0, 0, 0],
          [5, 0, 0, 0, 0, 4, 1, 0, 3],
          [0, 6, 0, 0, 5, 0, 7, 2, 0],
          [0, 0, 0, 0, 0, 3, 0, 8, 0],
          [8, 0, 0, 4, 1, 7, 0, 0, 9],
          [0, 3, 0, 8, 0, 0, 0, 0, 0],
          [0, 5, 4, 0, 8, 0, 0, 7, 0],
          [3, 0, 6, 1, 0, 0, 0, 0, 2],
          [0, 0, 0, 7, 0, 0, 3, 0, 0]]
		  
solveSudoku(sudoku, 0, 0)

# this program will print all solutions of a given sudoku, given as a two dimensional array (matrix), where the 
# zeroes (0) mark empty cells. it will also work with any sudoku, with a side length, which has an exact root, 
# e.g. 4, 9, 16, 25, etc.
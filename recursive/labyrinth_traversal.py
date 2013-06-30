#!/bin/python

def printMatrix(matrix):
  totalRows = len(matrix)
  totalCols = len(matrix[0])
  
  for row in range(0, totalRows):
    currentRow = ""
    for col in range(0, totalCols):
      currentRow += matrix[row][col] + " "
    print currentRow

def traverseCell(matrix, row, col, steps):
  totalRows = len(matrix)
  totalCols = len(matrix[0])
  
  if row == totalRows or row == -1:
    return
  
  if col == totalCols or col == -1:
    return
  
  if matrix[row][col] == "f":
    print steps
    printMatrix(matrix)
    raw_input()
    return
  
  if matrix[row][col] != "*":
    return
  
  matrix[row][col] = "v"
  
  steps.append("r")
  traverseCell(matrix, row, col + 1, steps)
  steps.pop()
  
  steps.append("d")
  traverseCell(matrix, row + 1, col, steps)
  steps.pop()
  
  steps.append("l")
  traverseCell(matrix, row, col - 1, steps)
  steps.pop()
  
  steps.append("u")
  traverseCell(matrix, row - 1, col, steps)
  steps.pop()
  
  matrix[row][col] = "*"
  
  return

labyrinth = [["*", "*", "*", "w", "*"],
             ["*", "w", "*", "*", "*"],
             ["*", "*", "*", "*", "*"],
             ["*", "w", "w", "w", "*"],
             ["*", "*", "*", "*", "f"]]
             
printMatrix(labyrinth)

steps = []
traverseCell(labyrinth, 0, 0, steps)

# this program will find every possible path between two points of a labyrinth, denoted by a matrix (two-dimensional
# array) and print them. "w" marks a wall (unpassable cell), "*" marks a passable cell, "f" marks the finish, "v" 
# marks a visited cell.

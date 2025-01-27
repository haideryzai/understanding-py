# Create a 3x3 grid (list of lists) where each element is the product of its row and column indices.

grid = [[i * j for j in range(3)] for i in range(3)]

for row in grid:
    print(row)

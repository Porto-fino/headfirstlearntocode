height = 100
width = 100

grid_model = [0] * height
for i in range(height):
   grid_model[i] = [0] * width

def next_gen():
   global grid_model

   for i in range(0, height):
       for j in range (0, width):
           cell = 0
           print('Checking cell', i, j)
           count = count_neighbors(grid_model, i, j)


           if grid_model[i][j] == 0:
               if count == 3:
                   cell = 1 
           elif grid_model[i][j] == 1:
               if count == 2 or count == 3:
                   cell = 1

def count_neighbors(grid, row, col):

   count = 0
   if row-1 >= 0:
       if grid[row-1][col] == 1:
           count = count + 1
   if (row-1 >= 0) and (col-1 >= 0):
       if grid[row-1][col-1] == 1:
           count = count + 1
   if (row-1 >= 0) and (col+1 < width):
       if grid[row-1][col+1] == 1:
           count = count + 1
   if col-1 >= 0:
       if grid[row][col-1] == 1:
           count = count + 1
   if col + 1 < width:
       if grid[row][col+1] == 1:
           count = count + 1
   if row + 1 < height:
       if grid[row+1][col] == 1:
           count = count + 1
   if (row + 1 < height) and (col-1 >= 0):
       if grid[row+1][col-1] == 1:
           count = count + 1
   if (row + 1 < height) and (col+1 < width):
       if grid[row+1][col+1] == 1:
           count = count + 1
   return count



if __name__ == '__main__':
    next_gen()
#import time

#Printing elegant Sudoku 
def print_sudoku(sudoku_array):
    print("\n-----------------------------------------\n")
    for r in range(9):
        print(*sudoku_array[r])
    print("\n-----------------------------------------\n")

# Find Empty slot in the sudoku_array.
def find_empty_slot(sudoku_array,emptyList):
    for r in range(9):
        for c in range(9):
            if(sudoku_array[r][c]==0):
                emptyList[0]=r
                emptyList[1]=c
                return True
    return False

# find the Number present in passed row 
def find_present_number_row(sudoku_array,row,present_number):
    for r in range(9):
        if sudoku_array[row][r] != 0:
            if sudoku_array[row][r] not in present_number:
                present_number.append(sudoku_array[row][r])

# Find the number present in passed Coloumn
def find_present_number_col(sudoku_array,col,present_number):
    for c in range(9):
        if sudoku_array[c][col] != 0:
            if sudoku_array[c][col] not in present_number:
                present_number.append(sudoku_array[c][col])

# find the number present in 3x3 box

def find_present_number_box(sudoku_array,row,col,present_number):
    for i in range(3):
        for j in range(3):
            if sudoku_array[row+i][col+j] != 0:
                if sudoku_array[row+i][col+j] not in present_number:
                    present_number.append(sudoku_array[row+i][col+j])

# get the number other than the number present in the Row,Coloumn,and Box.

def populate_possible_number(present_number,possible_number):
    for n in range(1,10):
        if n not in present_number:
            possible_number.append(n)

    
 # Caller
def process_number(sudoku_array,row,col,present_number,possible_number):
  
  find_present_number_row(sudoku_array,row,present_number)
  find_present_number_col(sudoku_array,col,present_number)
  find_present_number_box(sudoku_array,row-row%3,col-col%3,present_number)
  populate_possible_number(present_number,possible_number)
  

def find_sol(sudoku_array):
  
  # Empty List
  emptyList=[0,0]
  
  if (not find_empty_slot(sudoku_array,emptyList)):
    return True

  # assigning Empty Row and Coloumn returned By find_empty_location()
  row=emptyList[0]
  col=emptyList[1]

  # Stores the Value present in the Row,Coloumn and Box
  present_number = [] 
  # Stores the Value possible in that Empty Slot[row][col] in the Row,Coloumn and Box
  possible_number = []

  process_number(sudoku_array,row,col,present_number,possible_number)

  # If there are No possible number to insert int the Empty slot
  # than our assumption was wrong had to Backtrack and assign another possible number
  # and go on
  if len(possible_number) > 0 :
    for num in possible_number:

      #Assuming Num as the correct solution for this empty slot
      #so writing num to that empty slot and proceding to the the solution
      sudoku_array[row][col] = num

      #Printing the Sudoku to See the Change
      #Comment it, if you want to see direct and quick result
      print_sudoku(sudoku_array)
      
      #Moving onto the next Solution for the new Slot
      if(find_sol(sudoku_array)):
        return True
    
      #Assumption was wrong , rollbacking the change
      sudoku_array[row][col] = 0
  
  else:
  	# Backtracking
      return False


sudoku_array=[[0,0,0,0,0,8,0,0,0],
          [5,9,6,0,3,0,0,7,8],
          [3,0,2,5,1,0,0,6,0],
          [0,0,9,0,0,5,0,2,6],
          [8,0,0,9,0,6,0,0,1],
          [6,4,0,2,0,0,5,0,0],
          [0,7,0,0,5,1,6,0,9],
          [1,5,0,0,6,0,4,8,2],
          [0,0,0,3,0,0,0,0,0]]

# Uncomment if you want to BenchMark
#start_time = time.time()
find_sol(sudoku_array)
print_sudoku(sudoku_array)
#print("--- %s seconds ---" % (time.time() - start_time))

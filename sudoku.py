#using backtracking algorithm to solve a sudoku
board = [
    [3,0,0,0,8,0,0,0,9],
    [0,0,0,0,0,4,0,0,0],
    [1,8,0,5,0,0,2,0,0],
    [0,7,0,1,4,0,0,0,0],
    [0,0,3,0,0,0,0,0,2],
    [0,2,0,8,0,0,6,0,0],
    [0,0,0,0,0,0,5,9,0],
    [6,0,4,0,0,8,0,0,0],
    [0,0,7,9,0,0,0,0,0]
]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10): #check all possible values
        if valid(bo, i, (row, col)):
            bo[row][col] = i # change the number to i

            if solve(bo): 
            #here I use backtracking algotithm, if true, then we've solved the board
            #otherwise, we return false and reset the number and go to the previous call
                return True

            bo[row][col] = 0 # change the number to 0

    return False   # if all numbers don't work, return false


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, col
    
    return None

def valid(bo, num, pos):
    
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and i != pos[1]:
            return False

    #check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and i != pos[0]:
            return False
    
    #check square

    x = pos[1] // 3
    y = pos[0] // 3

    for i in range(y*3, y*3 + 3):
        for j in range(x*3, x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    
    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-------------------")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end = "")
            if j == len(bo[0])-1:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = "")
        

def check_solver(bo):
    print_board(bo)
    print("          ")
    solve(bo)
    if find_empty(bo):
        print("No solution")
    else:
        print_board(bo)

check_solver(board)



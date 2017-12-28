#!/usr/bin/env python
# a0.py : Solve the N-Queens or N-Rooks problem!
# Surbhi Paithankar, 2017

# This program uses D Crandall's nrooks-2.py program as a basic version.

# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.

# The N-Queens problem is: Given an empty NxN chessboard, place N Queens on the board so that no queens
# can take any other, i.e. such that no two queens share the same row or column or diagonal.

#This program takes 4 argument: 
#1. Problem type (nqueen/nrook) 2. Number of queens/rooks to be placed. 3.row number of Unavailable cell 4. Col number of unavailable cell 


import sys
 

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] ) 

# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] ) 

# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# Return a string with the board rendered in a human-friendly format: (Q for queen, R for rook, X for unavailable position, _ otherwise)
def print_board(board):
    str=""
    for row in board:
        for square in row:
            if square == -1:
                str+="X "
            elif square==0:
                str+="_ "
            else:
                if (prob_type=="nqueen"):
                    str+="Q "
                else:
                    str+="R "
        str+= "\n"
    return str
  
# Check if the state generated after adding a piece leads towards the goal or not.
# Checks if the state has not been already traversed, count of pieces on row and board doesn't exceed 1 and number of pieces on board in less than N.
def close_to_goal(old_board,new_board,r,c):
    return ((new_board!=old_board) and (count_pieces(new_board) <= N) and (count_on_row(new_board, r) == 1  ) and ( count_on_col(new_board, c) == 1 ))


# Add a piece to the board at the given position,if it can lead to a goal, and return a new board (doesn't change original).
# Incase of nqueens, we also check for number of pieces in the diagonals is not more than 1. It also checks if the state has not been visited previously.
def add_piece(board, row, col):
  if (ex_row==-1 and ex_col==-1) or not(row==ex_row and col==ex_col):
          new_board=  board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]
          if prob_type == "nqueen":
              if close_to_goal(board,new_board,row,col)==1 and diagonal_check(board,row,col)==0 and (new_board not in history1):
                  return new_board
          
          elif prob_type == "nrook":
              if close_to_goal(board,new_board,row,col):
                  return new_board
      

# Get list of successors of given board state 
def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]

# Check if board is a goal state.
# Check if all N pieces have been placed. 
# Note that, for other conditions like number of pieces on row,col and diagonals, we already checked them while placing a piece on the board. 
def is_goal(board):
    return count_pieces(board) == N

# Check if piece exists in the upper left diagonal from a given position on board.
def checkul(board,row,col):
   i = row
   j = col
   while (i>=0) and (j>=0):
     if(board[i][j]==1):
       return 1
     i = i-1
     j = j-1
   return 0

# Check if piece exists in the lower right diagonal from a given position on board.
def checklr(board,row,col):
   i = row
   j = col
   while (i<N) and (j<N):
     if(board[i][j]==1):
       return 1
     i = i+1
     j = j+1
   return 0


# Check if piece exists in the upper right diagonal from a given position on board.
def checkur(board,row,col):
   i = row
   j = col
   while (i>=0) and (j<N):
     if(board[i][j]==1):
       return 1
     i = i-1
     j = j+1
   return 0

# Check if piece exists in the lower left diagonal from a given position on board.
def checkll(board,row,col):
   i = row
   j = col
   while (i<N) and (j>=0):
     if(board[i][j]==1):
       return 1
     i = i+1
     j = j-1
   return 0

# Check if piece exists in any of the four diagonal directions from a given position on board.
def diagonal_check(board,row,col):
   return checkll(board,row,col) or checkur(board,row,col) or checklr(board,row,col) or checkul(board,row,col)


# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]

    while len(fringe) > 0:
        for s in successors( fringe.pop() ):
            if s:
                if is_goal(s):
                    return(s)
                fringe.append(s)
                history1.append(s)
    return False

# This is to specify if the problem type is nrook or nqueen.
prob_type = str(sys.argv[1])
if not(prob_type=="nrook" or "nqueen"):
  print "Kindly enter a valid problem."
# This is N, the size of the board. It is passed through command line arguments.
N = int(sys.argv[2])

# This is the row number of the unavailable position.
ex_row = int(sys.argv[3])-1
#This is the column number of the unavailable position.
ex_col = int(sys.argv[4])-1


# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N]*N
history1 = []

#This is to print the initial board. Stores -1 and later displays X for the unavailable position on the initial board.
#We do not change the original board.
if not(prob_type=="nrook" or prob_type=="nqueen"):
  print "Kindly enter a valid problem.(nqueen/nrook)"
else:
  initial = initial_board
  for row in range(0,N):
      for col in range(0,N):
          if (row==ex_row) and (col==ex_col):
                initial=  initial[0:row] + [initial[row][0:col] + [-1,] + initial[row][col+1:]] + initial[row+1:]
  print ("Starting from initial board:\n" + print_board(initial) + "\n\nLooking for solution...\n")


# Solve the problem!
  solution = solve(initial_board)

#This is to print the solution board, if exists.
  answer = solution
  for row in range(0,N):
      for col in range(0,N):
         if answer: 
             if (row==ex_row and col==ex_col):
                 answer=  answer[0:row] + [answer[row][0:col] + [-1,] + answer[row][col+1:]] + answer[row+1:]
  print (print_board(answer) if solution else "Sorry, no solution found. :(")


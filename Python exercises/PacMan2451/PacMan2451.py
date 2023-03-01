"""
Problem - 2451 - Beecrowd
Code made by Miguel Rios Tangarife

PacMan wants to eat a lot of points 'o' 
but if PacMam meets with a ghost 'A' 
the ghost steals all his points from pacman

In this game you are playing on a board represented by a square matrix
'.' mean an empty space from the board

Pacman moves through the matrix in a zigzag pattern starting at the top left corner 
This code tells us how much food pacman collected on his journey!

"""
board_size = int(input()) #Request to the user for an integer number  
board = [] 
for i in range(board_size): #Iterate n times to enter the rows of the board
    while True:
        row = input()
        #If the row does not have the correct size, it does not allow the row to be entered
        if len(row) != board_size:
            print()
        #If the row contains the correct size, it enters it into the matrix
        else:
            break
    board.append(list(row))
#Obtain the size of the board and Define the score variables initially to 0
size = len(board)
max_counter = 0
counter = 0

#Define PacMan's path while keeping track of the moment where it obtains the highest amount of food
for i in range(size):
            if i % 2 == 0: 
                for j in range(size):
                    if board[i][j] == "o":
                        counter += 1 # Add food when seeing an 'o'
                        if counter > max_counter:
                            max_counter = counter
                    elif board[i][j] == "A":# Loose food when seeing an 'A'
                        counter = 0
            else: 
                for j in range(size-1,-1,-1): # Iterate over a sequence of values in reverse order starting at size-1
                    if board[i][j] == "o":
                        counter += 1
                        if counter > max_counter:
                            max_counter = counter
                    elif board[i][j] == "A":
                        counter = 0
print(f"{max_counter}")


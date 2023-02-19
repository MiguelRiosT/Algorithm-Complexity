
def board_size():
    """
    This function promts the users to enter a board size for a square matrix
    conditions for entering the size: 
    -Board size must be between 2 and 100
    exceptions that may occur:
    -the size of the board does not accept decimal numbers
    """
    while True:
         size = input("Board size: ")
         try:
            size = int(size) #User request
            if (size>=2 and size<=100): 
                return size
            else:
                print("Board size must be between 2 and 100")
         except ValueError:
            print("Board size must be an int number ")

def board():
    """
    This function considers the size input by the user
    and with that size it makes the square matrix
    """
    size = board_size() #To get the value of size using board_size() function
    board = []
    allowed_values = ["A", "o", "."] 
    for i in range(size):
        row = []
        for j in range(size):
            if i==0 and j==0: # When the position of the matrix is [0][0], the only accepted value is '.'
                value=""
                while value != ".":
                    value= input(f"[{i}][{j}]: ")
                row.append(value)
            else:
                value = ""
                while value not in allowed_values: # When position of the matrix is not [0][0], Only values from the list of allowed_values are accepted
                    value = input(f"[{i}][{j}]: ")
                row.append(value)
        board.append(row)
    print("Board: ") #show the board with all values 
    for row in board:
        print(" ".join(str(value) for value in row))#The code displays the matrix in the console, separating the values by white spaces
    return board


def pacman_filled(board):
        """
        Pacman follow the next path:
        1. Start in the upper left corner
        2. Pacman run from left to right
        3. Pacman down one position and run from right to left
        4. Pacman maintains that movement pattern
        """
        size = len(board)
        max_counter = 0
        counter = 0
        for i in range(size):
            if i % 2 == 0:
                for j in range(size):
                    if board[i][j] == "o":
                        counter += 1
                        if counter > max_counter:
                            max_counter = counter
                    elif board[i][j] == "A":
                        counter = 0
            else:
                for j in range(size-1,-1,-1):
                    if board[i][j] == "o":
                        counter += 1
                        if counter > max_counter:
                            max_counter = counter
                    elif board[i][j] == "A":
                        counter = 0
        return max_counter   

board = board()
pacman_filled(board)
max_counter = pacman_filled(board)
print(f"{max_counter}")









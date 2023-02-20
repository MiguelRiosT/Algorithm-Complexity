board_size = int(input()) #Request to the user for an integer number  
board = [] 
for i in range(board_size): #Itera n veces para ingresar las filas del tablero
    while True:
        row = input()
        #Si la fila no tiene el tamaño correcto no permite ingresar la fila
        if len(row) != board_size:
            print()
        #Si la fila contiene el tamaño correcto la ingresa a la matrix
        else:
            break
    board.append(list(row))
#Obtain the size of the board y define las variables de puntaje inicialmente en 0
size = len(board)
max_counter = 0
counter = 0

for i in range(size):
    #Si la fila es par, itera sobre las columnas de izquierda a derecha
            if i % 2 == 0: #itera sobre las columnas de izquierda a derecha
                for j in range(size):
                    if board[i][j] == "o":
                        counter += 1
                        if counter > max_counter:
                            max_counter = counter
                    elif board[i][j] == "A":
                        counter = 0
            else: #itera sobre las columnas de derecha a izquierda
                for j in range(size-1,-1,-1): # iterar sobre una secuencia de valores en orden inverso iniciando en size-1
                    if board[i][j] == "o":
                        counter += 1
                        if counter > max_counter:
                            max_counter = counter
                    elif board[i][j] == "A":
                        counter = 0
print(f"{max_counter}")
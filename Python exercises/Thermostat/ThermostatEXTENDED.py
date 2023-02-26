#NUMERO DE CASOS DE PRUEBA
while True:
    try:
        t = int(input("Ingrese un número entero único en el rango de 1 a 10^4: "))
        if t < 1 or t > 10**4:
            print("El número debe estar dentro del rango especificado.")
        else:
            break
    except ValueError:
        print("Por favor, ingrese un número entero.")
output=[]
for i in range(t):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    if a == b:
        output.append(0)
    elif abs(a-b) >= x:
        output.append(1) 
    elif r - max(a, b) >= x or min(a, b) - l >= x:
        output.append(2)
    elif r - b >= x and a - l >= x or r - a >= x and b - l >= x:
        output.append(3)
    else:
        output.append(-1)
for elem in output: 
    print(elem)
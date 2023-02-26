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

#PRIMERA Y SEGUNDA LINEA DE INPUT
l, r, x = map(int, input("Ingrese los valores de la primera línea separados por espacios: ").split())
# Pedimos al usuario que ingrese los valores de la segunda línea
a, b = map(int, input("Ingrese los valores de la segunda línea separados por espacios: ").split())
# Imprimimos los valores para verificar que se hayan leído correctamente
print("l =", l)
print("r =", r)
print("x =", x)
print("a =", a)
print("b =", b)
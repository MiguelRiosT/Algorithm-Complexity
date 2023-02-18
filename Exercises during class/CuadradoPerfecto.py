#Cuadrados perfectos

#Averiguar si un número natural m es un cuadrado perfecto 
#Cuadrado perfecto m = n2
import math
m = int(input("m: "))
n = math.sqrt(m)
print(n)
if m == n**2:
    print("m es un cuadrado perfecto")
else:
    print("m no es un cuadrado perfecto")
    
#Cuadrado perfecto previo
a = int(input("a: "))
b = math.sqrt(a)
redondeo = math.floor(b)
print("El cuadrado perfecto previo es: ")
print(redondeo)
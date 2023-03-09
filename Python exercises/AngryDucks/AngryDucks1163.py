"""
Angry Ducks - Exercise 1163 - Beecrowd
Code made by: Miguel Rios Tangarife
Nlogony city and Ducklogony city are in war
Ducknese people make a slingshot and ask you to say if with the correct values they will hit the Nloogny city
Slingshot! 
h --> height
p1 --> points wehere the Nlogony city begins 
p2 --> points wehere the Nlogony city ends
a -->the shooting angle
v -->launching speed
we assume the following values g=9.80332 and n=3.14159
we need to calculate if the projectile will hit the target
"""

#Definamos las constantes
g= 9.80665
pi= 3.14159

#Calculos matematicos


#Pedimos las primeras lineas
h = float(input())
p1,p2 = map(int, input().split())
n= int(input())

#En el for vamos a calcular si es NUCK O DUCK
for i in range(n):
    #pedimos las otras dos variables que faltan
    a, v = map(float, input().split())




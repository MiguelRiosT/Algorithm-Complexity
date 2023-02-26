resultados=[]
t=int(input())
for i in range(t):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    erremenosequis= r-x #porque r rango maximo y x minimo 
    absDiffmayorque= abs(a-b) >= x #Entrega un falso o un verdadero
    absDiffmenorque= abs(a-b) <= x #Entrega un falso o un verdadero 
    rangelbr=l<=b<=r #Entrega un falso o un verdader
    if a == b:
        resultados.append(0)
    elif absDiffmayorque and rangelbr:
        resultados.append(1) 
    elif x == b:
        resultados.append(2)
    elif erremenosequis > 0:
        resultados.append(3)
    elif erremenosequis < 0:
        resultados.append(-1)
    else:
        print()
for elem in resultados:
    print(elem)
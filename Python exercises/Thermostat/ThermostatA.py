resultados=[]
t=int(input())
for i in range(t):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    if a == b:#0
        resultados.append(0)
    elif abs(a-b) >= x and l<=b<=r:#1
        resultados.append(1) 
    elif x == b:#2
        resultados.append(2)
    elif r-x > 0:#3
        resultados.append(3)
    elif r-x < 0:#-1
        resultados.append(-1)
    else:
        print()
for elem in resultados: 
    print(elem)
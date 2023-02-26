"""
def solve():
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    if a == b:
        return 0
    if abs(a - b) >= x:
        return 1
    if r - max(a, b) >= x or min(a, b) - l >= x:
        return 2
    if r - b >= x and a - l >= x or r - a >= x and b - l >= x:
        return 3
    return -1
t = int(input())
for _ in range(t):
    print(solve())
"""
resultados=[]
t=int(input())
for i in range(t):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    if a == b:#0
        resultados.append(0)
    elif abs(a-b) >= x:#1
        resultados.append(1) 
    elif r - max(a, b) >= x or min(a, b) - l >= x:#2
        resultados.append(2)
    elif r - b >= x and a - l >= x or r - a >= x and b - l >= x:#3
        resultados.append(3)
    else:
        resultados.append(-1)
for elem in resultados: 
    print(elem)
"""
Angry Ducks - Exercise 1163 - Beecrowd
Code made by: Miguel Rios Tangarife
Nlogony city and Ducklogony city are in war
Ducknese people make a slingshot and ask you to say if with the correct values they will hit the Nloogny city
Slingshot! 
h --> height
p1 --> points wehere the Nlogony city begins 
p2 --> points wehere the Nlogony city ends
a -->the shooting angle in grades
v -->launching speed
we assume the following values g=9.80332 and n=3.14159
we need to calculate if the projectile will hit the target
"""
g = 9.80665
pi = 3.14159
#Taylor Series
def sin(x):
    x = x % (2 * pi)
    result = 0
    for i in range(10):
        sign = (-1) ** i
        coeff = x ** (2 * i + 1)
        fact = 1
        for j in range(2 * i + 1):
            fact *= j + 1
        result += sign * coeff / fact
    return result

def cos(x):
    x = x % (2 * pi)
    result = 0
    for i in range(10):
        sign = (-1) ** i
        coeff = x ** (2 * i)
        fact = 1
        for j in range(2 * i):
            fact *= j + 1
        result += sign * coeff / fact
    return result

def max_distance(h, alpha, v):
    alpha = alpha * pi / 180
    d = ((v**2) * sin(2*alpha)) / g #for y=0 when h final is 0
    x = d+h
    return x


h = float(input())
p1, p2 = map(int, input().split())
n = int(input())

outputs = []


for i in range(n):
    alpha, v = map(float, input().split())
    d_proj = max_distance(h, alpha, v)

    if p1 <= d_proj <= p2:
        outputs.append("{:.5f} -> DUCK".format(d_proj))
    else:
        outputs.append("{:.5f} -> NUCK".format(d_proj))

print("\n".join(outputs))
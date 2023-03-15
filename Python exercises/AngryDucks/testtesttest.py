import math
g = 9.80665
pi = 3.14159

"""
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
"""


h = float(input())
p1, p2 = map(int, input().split())
n = int(input())

outputs = []


for i in range(n):
    alpha,initial_speed = map(float,input().split())
    #Calculations
    alpha = alpha * pi / 180 
    initial_speed_x= initial_speed * math.cos(alpha) 
    initial_speed_y= initial_speed * math.sin(alpha)
    height_max = (initial_speed_y**2)/(g*2) + h
    final_speed_y = (2*g*height_max)**0.5
    fly_time = initial_speed_y / g 
    down_time = final_speed_y / g 
    total_time = fly_time + down_time 
    final_position_X = initial_speed_x * total_time
             

    if p1 <= final_position_X <= p2:
        outputs.append("{:.5f} -> DUCK".format(final_position_X))
    else:
        outputs.append("{:.5f} -> NUCK".format(final_position_X))

print("\n".join(outputs))
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
import math
g= 9.80665
pi= 3.14159

def max_distance(h,alpha, speed):
    alpha = math.radians(alpha)  
    initial_speed_x = speed * math.cos(alpha) 
    initial_speed_y = speed * math.sin(alpha)
    heightMax = (initial_speed_y**2)/(g*2) + h
    final_speed_y = (2*g*heightMax)**0.5
    fly_time = initial_speed_y / g #Fly time
    down_time = final_speed_y / g #Down time
    total_time = fly_time + down_time #Total time
    final_X = initial_speed_x * total_time
    return final_X

h = float(input())#Initial Height
p1, p2 = map(int, input().split()) #Begins and Ends distance
n = int(input())# Number of try
#outputs = []

for i in range(n):
    alpha, speed = map(float, input().split())#angle and speed
    calculate_distance_hit = max_distance(h, alpha, speed)

    if p1 < calculate_distance_hit < p2:
        print("{:.5f} -> DUCK".format(calculate_distance_hit))
        #outputs.append("{:.5f} -> DUCK".format(calculate_distance_hit))
    else:
        print("{:.5f} -> DUCK".format(calculate_distance_hit))
        #outputs.append("{:.5f} -> NUCK".format(calculate_distance_hit))

#print("\n".join(outputs))


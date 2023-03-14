"""
Angry Ducks - Exercise 1163 - Beecrowd
Code made by: Miguel Rios Tangarife
Nlogony city and Ducklogony city are in war
Ducknese people make a slingshot and ask you to say if with the correct values they will hit the Nloogny city
Slingshot! 
h --> height
p1 --> start point
p2 --> end point
a -->the shooting angle in grades
v -->launching speed
we assume the following values g=9.80332 and n=3.14159
we need to calculate if the projectile will hit the target
if we hit DUCK!
else NUCK!
"""
import math
pi =  3.14159
g = 9.80665
while True:
    try:
        initial_height = float(input()) 
        start_point,end_point = map(int,input().split()) 
        t = int(input()) 
        for i in range(t):
            alpha,initial_speed = map(float,input().split())
            #Calculations
            alpha = alpha * pi / 180 
            initial_speed_x= initial_speed * math.cos(alpha) 
            initial_speed_y= initial_speed * math.sin(alpha)
            height_max = (initial_speed_y**2)/(g*2) + initial_height
            final_speed_y = (2*g*height_max)**0.5
            fly_time = initial_speed_y / g 
            down_time = final_speed_y / g 
            total_time = fly_time + down_time 
            final_position_X = initial_speed_x * total_time

            print("{:.5f} -> DUCK".format(final_position_X)) if start_point < final_position_X < end_point else print("{:.5f} -> NUCK".format(final_position_X))
    except EOFError:
        break
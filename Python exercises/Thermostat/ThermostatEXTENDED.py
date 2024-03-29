"""
Problem - 1759C - Codeforces
Code made by Miguel Rios Tangarife
In this problem we have an old thermostat and we need to find the minimum number of operations required 
to get temperature b from temperature a, or say that it is impossible

In the exercise we are given the variables:
L,r,x  where L,r are the range of temperature and 
x is the minimum temperature change 
a,b -->(initial temperature, final temperature)

This is another way to do Thermostat exercise
"""

#Number of test cases
while True:
    try:
        t = int(input())
        if t <= 1 or t >= 10**4: #((1≤t≤10^4)) 
            print("The number must be within the specified range.")
        else:
            break
    except ValueError:
        print("Please enter an integer number")

output=[] #List containing the output values ​​that are saved with each for iteration
for i in range(t):
    l, r, x = map(int, input().split()) #Allows inputs to be entered like this: 3 5 6
    a, b = map(int, input().split()) 
    if a == b: #When this happen the thermostat is already set up correctly
        output.append(0)# Add the number of operations required in the output list 
    elif abs(a-b) >= x:
        output.append(1) 
    elif r - max(a, b) >= x or min(a, b) - l >= x:
        output.append(2)
    elif r - b >= x and a - l >= x or r - a >= x and b - l >= x:
        output.append(3)
    else:
        output.append(-1)
for elem in output: #Display the data in an ordered way
    print(elem)
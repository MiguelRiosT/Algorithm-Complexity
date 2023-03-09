import math

# Constants
g = 9.80665
pi = 3.14159

# Function to calculate the maximum distance that a projectile can reach
def calculate_distance(h, alpha, v):
    # Convert the angle from degrees to radians
    alpha = math.radians(alpha)

    # Calculate the time that the projectile stays in the air
    t = (v * math.sin(alpha) + math.sqrt((v * math.sin(alpha))**2 + 2 * g * h)) / g

    # Calculate the maximum distance that the projectile can reach
    d = v * math.cos(alpha) * t

    return d

# Loop to read the input and process each test case
while True:
    try:
        # Read the input values for the current test case
        h = float(input())
        p1, p2 = map(int, input().split())
        n = int(input())

        # Loop to process each try
        for i in range(n):
            # Read the input values for the current try
            alpha, v = map(float, input().split())

            # Calculate the distance that the projectile can reach
            d = calculate_distance(h, alpha, v)

            # Check if the projectile hits Nlogony
            if d >= p1 and d <= p2:
                print("{:.5f} -> DUCK".format(d))
            else:
                print("{:.5f} -> NUCK".format(d))
    except:
        break
"""
Exercises during class
Code made by Miguel Rios Tangarife

We want to determine whether an integer entered through the console is a perfect square. 
If it is not, then it is not a perfect square. 
Additionally, we want to find the previous perfect square.
"""
import math
def perfect_square():
    print("PERFECT SQUARE?")
    m = int(input("m: "))
    square_root=math.sqrt(m)
    if round(square_root)**2 == m:
        print("IS A PERFECT SQUARE")
    else:
        print("IS NOT A PERFECT SQUARE")

def previous_perfect_square():
     print("What is the previous perfect square of m?")
     m = int(input("m: "))
     n = math.sqrt(m)   
     rounding = math.floor(n)
     print("The previous perfect square of m = ",m, "is ", rounding**2)
     print(rounding**2,"is ",rounding,"*",rounding)

perfect_square()
previous_perfect_square()


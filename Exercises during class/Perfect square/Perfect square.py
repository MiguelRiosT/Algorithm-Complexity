#Perfect square
#To determine if a user-input m is a perfect square
import math

def perfect_square():
    print("PERFECT SQUARE")
    m = int(input("m: "))
    square_root=math.sqrt(m)#Take the square root of m

    if square_root**2 == m:#Square the variable square_root and compare with m
        print("Is a perfect square")
    else:
        print("Is not a perfect square")

#Previous perfect square
def previous_perfect_square():
     print("PREVIOUS PERFECT SQUARE")
     m = int(input("m: "))
     n = math.sqrt(m)   
     rounding = math.floor(n)#Round down
     print("The previous perfect square is: ")
     print(rounding)

perfect_square()
previous_perfect_square()


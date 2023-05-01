"""
Exercises during class
Code made by Miguel Rios Tangarife

We want to determine whether an integer entered through the console is a perfect square. 
If it is not, then it is not a perfect square. 
Additionally, we want to find the previous perfect square.
In this case we don't use the library math
"""
def perfect_square():
    print("PERFECT SQUARE?")
    m = int(input("m: "))
    i = 1
    while i*i <= m:
        if i*i == m:
            print("IS A PERFECT SQUARE")
            return
        i += 1
    print("IS NOT A PERFECT SQUARE")

def previous_perfect_square():
    print("What is the previous perfect square of m?")
    m = int(input("m: "))
    i = 1
    while i*i < m:
        i += 1
    i -= 1
    print("The previous perfect square of m = ", m, "is", i*i)

perfect_square()
previous_perfect_square()
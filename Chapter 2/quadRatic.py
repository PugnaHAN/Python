import cmath
import math
import sys

def getInput(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
    return x

def getResult(a, b, c):
    x1 = None
    x2 = None
    discriminant = b**2 - 4*a*c
    if discriminant == 0:
        x1 = -(b/(2*a))
        x2 = x1
    else:
        if discriminant > 0:
            root = math.sqrt(discriminant)
        else:
            root = cmath.sqrt(discriminant)
        x1 = (-b + root)/(2*a)
        x2 = (-b - root)/(2*a)

    return (x1, x2)

print("ax\N{SUPERSCRIPT TWO} + bx +c = 0")
a = getInput("enter a: ", False)
b = getInput("enter b: ", False)
c = getInput("enter c: ", False)
result = getResult(a, b, c)

print("{0}x\N{SUPERSCRIPT TWO}{1:+}x{2:+} = 0".format(a, b, c), end = " ")
print("\N{RIGHTWARDS ARROW}", end = " ")
print("x1 = {}, x2 = {}".format(result[0], result[1]))

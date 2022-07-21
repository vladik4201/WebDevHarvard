import sys

try:
    x = int(input("x value"))
    y = int(input("y value"))
except ValueError:
    print("Error, please enter a number")
    sys.exit(1)

try:
    result = x/y 

except ZeroDivisionError:
    print("Error can't divide by 0")
    sys.exit(1)


print(f"{x} divided by {y} equals {result}")

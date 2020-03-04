def whileLoop(base, expressions):
    multiplier = 1
    while multiplier <= expressions:
        print(str(base) + " * " + str(multiplier) + " = " + str(base * multiplier))
        multiplier = multiplier + 1

def getValue(name):
    print("Enter " + name + " value")
    value = int(input())
    
    return value

# Main
# This program uses a loop to generate a list of multiplication expressions for a given value.
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Loops
base = getValue("base")
expressions = getValue("expressions")
whileLoop(base, expressions)

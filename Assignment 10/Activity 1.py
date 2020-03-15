def forLoop(base, expressions):
    for count in range(1, expressions + 1, 1):
        print(str(base) + " * " + str(count) + " = " + str(base * count))

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
forLoop(base, expressions)

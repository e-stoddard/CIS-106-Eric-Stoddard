def doLoop(base, expressions):
    count = expressions
    while True:    #This simulates a Do Loop
        print(str(base) + " * " + str(count) + " = " + str(base * count))
        count = count - 1
        if not(count > 0): break   #Exit loop

def getValue(name):
    print("Enter " + name + " value")
    value = int(input())
    
    return value

# Main
# This program uses a loop to generate a list of multiplication expressions for a given value.
base = getValue("base")
expressions = getValue("expressions")
doLoop(base, expressions)

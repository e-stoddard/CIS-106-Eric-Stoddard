def getValue(name):
    print("Enter " + name + " value")
    value = int(input())
    
    return value

def nestedLoop(start, end):
    for row in range(start, end + 1, 1):
        print("     " + str(row), end='', flush=True)
    print("   ")
    for column in range(start, end + 1, 1):
        print(str(column) + "   ", end='', flush=True)
        for row in range(start, end + 1, 1):
            print(str(row * column) + "   ", end='', flush=True)
        print("   ")

# Main
# This Program will create a multiplication table from a given range of numbers.
# References:
# 
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Loops
# 
# https://www.youtube.com/watch?v=H7frvcAHXps
start = getValue("starting")
end = getValue("ending")
nestedLoop(start, end)

def getQuantity():
    print("Enter the total number of grades")
    quantity = int(input())
    
    return quantity

def whileLoop(quantity):
    total = 0
    counter = 0
    while counter < quantity:
        print("Enter grade")
        grade = int(input())
        total = total + grade
        counter = counter + 1
    print("Average grade = " + str(float(total) / quantity))

# Main
# This program will calculate the average grade from a specified total number of grades.
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Loops
quantity = getQuantity()
whileLoop(quantity)

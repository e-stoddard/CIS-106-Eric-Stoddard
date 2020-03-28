def getQuantity():
    print("Enter the total number of grades")
    quantity = int(input())
    return quantity


def whileLoop(quantity):
    grades = [None] * quantity
    counter = 0
    while counter < quantity:
        print("Enter grade")
        grades[counter] = int(input())
        counter = counter + 1
    grades.sort()
    return grades


def DisplayHigh(grades, quantity):
    print("High grade = " + str(grades[quantity - 1]))


def DisplayLow(grades):
    print("Low grade = " + str(grades[0]))


def DisplayAverage(grades, quantity):
    total = sum(grades)
    print("Average grade = " + str(total / quantity))


def main():
    quantity = getQuantity()
    grades = whileLoop(quantity)
    DisplayHigh(grades, quantity)
    DisplayLow(grades)
    DisplayAverage(grades, quantity)


# This program will calculate and display the high, low and average grade
# from a static list of grades.
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Loops
# https://press.rebus.community/programmingfundamentals/

main()

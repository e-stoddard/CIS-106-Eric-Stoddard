def GetQuantity():
    print("Enter the total number of grades")
    quantity = int(input())
    return quantity


def WhileLoop(quantity):
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


def DisplayGrades(grades):
    for index in range(len(grades)):
        print("Grade[" + str(index) + "] = " +
              str(grades[index]))


def main():
    quantity = GetQuantity()
    grades = WhileLoop(quantity)
    DisplayGrades(grades)
    DisplayHigh(grades, quantity)
    DisplayLow(grades)
    DisplayAverage(grades, quantity)


# This program will calculate and display the high, low and average grade
# from a static list of grades.
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Loops
# https://press.rebus.community/programmingfundamentals/

main()

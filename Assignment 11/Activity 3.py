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


def DisplayLow(grades, quantity):
    print("Low grade = " + str(grades[quantity - 1]))


def DisplayHigh(grades):
    print("High grade = " + str(grades[0]))


def DisplayAverage(grades, quantity):
    total = sum(grades)
    print("Average grade = " + str(total / quantity))


def DisplayGrades(grades):
    grades.reverse()
    for index in range(len(grades)):
        print("Grade[" + str(index) + "] = " +
              str(grades[index]))


def main():
    quantity = GetQuantity()
    grades = WhileLoop(quantity)
    DisplayGrades(grades)
    DisplayHigh(grades)
    DisplayLow(grades, quantity)
    DisplayAverage(grades, quantity)


# This program will calculate and display the high, low and average grade
# from a static list of grades.
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Loops
# https://press.rebus.community/programmingfundamentals/
# https://www.programiz.com/python-programming/methods/list/reverse

main()

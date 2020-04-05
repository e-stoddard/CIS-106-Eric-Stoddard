def collect_grades():
    grade_list = []
    counter = 0
    while counter >= 0:
        print("Enter grade")
        grade = int(input())
        if grade >= 0:
            grade_list.append(grade)
            counter = counter + 1
        else:
            counter = -1
    grade_list.sort()
    return grade_list


def display_high(grade_list):
    print("High grade = " + str(grade_list[len(grade_list) - 1]))


def display_low(grade_list):
    print("Low grade = " + str(grade_list[0]))


def display_average(grade_list):
    total = sum(grade_list)
    print("Average grade = " + str(total / len(grade_list)))


def main():
    grade_list = collect_grades()
    display_high(grade_list)
    display_low(grade_list)
    display_average(grade_list)


# This program will calculate and display the high, low and average grade
# from a dynamic list of grades.
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Loops
# https://press.rebus.community/programmingfundamentals/

main()

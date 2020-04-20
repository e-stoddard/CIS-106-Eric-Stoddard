# This program will display high, low and average scores
# based on input from scores.txt
# References:
# https://stackoverflow.com/questions/7422453/
# python-change-type-of-whole-list
# https://stackoverflow.com/questions/43578530/python-creating-
# parallel-lists-from-a-text-file
# https://www.w3schools.com/python/python_file_open.asp
# https://press.rebus.community/programmingfundamentals/
# https://stackoverflow.com/questions/20457038/how-to-round-
# to-2-decimals-with-python


def get_file():
    scores = open("scores.txt", "r+")
    title = scores.readline()
    str = scores.read()
    individual = str.split("\n")
    grades = []
    names = []
    for i in individual:
        name_score = i.split(",")
        names.append(name_score[0])
        grades.append(name_score[1])
    return grades


def convert_grades(grades):
    grades_float = []
    for i in range(len(grades)):
        grades[i] = float(grades[i])
        grades_float.append(grades[i])
    return grades_float


def display_high(grades_float):
    grades_float.sort(reverse=True)
    print("High score = " + str(grades_float[0]))


def display_low(grades_float):
    grades_float.sort()
    print("Low score =" + str(grades_float[0]))


def display_average(grades_float):
    total = sum(grades_float)
    average = total / len(grades_float)
    print("Average grade = " + str(round(average, 2)))


def main():
    grades = get_file()
    grades_float = convert_grades(grades)
    print(grades_float)
    display_high(grades_float)
    display_low(grades_float)
    display_average(grades_float)


main()

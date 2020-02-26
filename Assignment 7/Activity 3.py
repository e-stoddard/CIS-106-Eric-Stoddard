# This program will convert a distance in miles to the users choice
# of either metric units (kilometers, meters, and centimeters) or
# US units (yards, feet, and inches).
#
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Conditions
# https://www.mathsisfun.com/measure/us-standard-length.html


def get_choice():
    print("Enter U to convert to US measurements or" +
          "enter M to convert to metric.")
    choice = input()
    return choice


def get_miles():
    print("Enter number of miles you would like to convert")
    miles = float(input())
    return miles


def process_us(miles):
    yards = miles * 1760
    feet = yards * 3
    inches = feet * 12
    display_result_us(miles, yards, feet, inches)


def process_metric(miles):
    kilometers = miles * 1.609344
    meters = kilometers * 1000
    centimeters = meters * 100
    display_result_metric(miles, kilometers, meters, centimeters)


def display_result_us(miles, yards, feet, inches):
    print(str(miles) + " miles is " + str(yards) + " yards " +
          str(feet) + " feet " + str(inches) + " inches")


def display_result_metric(miles, kilometers, meters, centimeters):
    print(str(miles) + " miles is " + str(kilometers) + " kilometers " +
          str(meters) + " meters " + str(centimeters) + " centimeters")


def main():
    miles = get_miles()
    choice = get_choice()
    if choice == "U" or choice == "u":
        process_us(miles)
    elif choice == "M" or choice == "m":
        process_metric(miles)
    else:
        print("You must enter U for US measurments" +
              "or M for metric measurments")


main()

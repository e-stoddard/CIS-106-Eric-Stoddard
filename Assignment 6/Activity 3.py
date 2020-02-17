def get_miles():
    print ("Enter distance in miles")
    miles = float(input())
    return miles


def calculate_yards(miles):
    yards = miles * 1760
    return yards


def calculate_feet(yards):
    feet = yards * 3
    return feet


def calculate_inches(feet):
    inches = feet * 12
    return inches


def display_result(miles, yards, feet, inches):
    print (str(miles) + " miles is equal to " + str(yards) +
           " yards, " + str(feet) + " feet and " +
           str(inches) + " inches.")


# Main
# This program will calculate yards, feet and inches from
# an input distance in miles
miles = get_miles()
yards = calculate_yards(miles)
feet = calculate_feet(yards)
inches = calculate_inches(feet)
display_result(miles, yards, feet, inches)

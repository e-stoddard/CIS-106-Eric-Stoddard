#This program will convert a distance in miles to the equivalent distance in yards, feet and inches
print ("Enter distance in miles")
miles = int(input())
yards = miles * 1760
feet = miles * 5280
inches = miles * 63360
print(str(miles) + " miles in equivalent to " + str(yards) + " yards, " + str(feet) + " feet, " + str(inches) + " inches")

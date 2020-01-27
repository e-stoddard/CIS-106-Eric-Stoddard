# This program will calculate the floor coverage of a rectangular room in square yards from an input width in feet and an input length in feet.
print("Enter width of the room (in feet)")
widthFeet = float(input())
print("Enter length of the room (in feet)")
lengthFeet = float(input())
widthMeters = widthFeet / 3
lengthMeters = lengthFeet / 3
squareYards = widthMeters * lengthMeters
print("A rectangular room that is " + str(widthFeet) + " ft. wide by " + str(lengthFeet) + " ft. long will have " + str(squareYards) + " square yards of floor coverage")

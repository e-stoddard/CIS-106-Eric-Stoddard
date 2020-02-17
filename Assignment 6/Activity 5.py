def get_width():
    print ("Enter the width of the room in feet")
    width = float(input()) / 3
    return width


def get_length():
    print ("Enter the length of the room in feet")
    length = float(input()) / 3
    return length


def calc_floor_space(length, width):
    floor_space = float(length * width)
    return floor_space


def display_result(floor_space):
    print ("This room will have " + str(floor_space) +
           " square yards of floor space")

# Main
# This program will calculate the floor coverage of a rectangular
# room in square yards from given dimensions in feet.
width = get_width()
length = get_length()
floor_space = calc_floor_space(length, width)
display_result(floor_space)

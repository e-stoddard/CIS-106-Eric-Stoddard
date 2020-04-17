# This program will take a first and last name and change
# it to the form "last name, first initial."
# References:
# https://press.rebus.community/programmingfundamentals/
# https://en.wikiversity.org/wiki/Programming_Fundamentals/
# Strings
# https://www.w3schools.com/python/python_ref_string.asp


def get_name():
    print("Enter first and last name")
    full_name = str(input())
    split_name = full_name.split(None, 1)
    print(split_name)
    return split_name


def find_last_name(split_name):
    last_name = split_name[1].strip().title()
    while "  " in last_name:
        last_name = last_name.replace("  ", " ")
    return last_name


def find_first_initial(split_name):
    first_name = split_name[0]
    first_initial = first_name[0].title()
    return first_initial


def display_name(last_name, first_initial):
    print(last_name + ",", first_initial + ".")


def main():
    split_name = get_name()
    first_initial = find_first_initial(split_name)
    last_name = find_last_name(split_name)
    display_name(last_name, first_initial)


main()

# This program will take a string of names seperated by commas and
# print each name on a seperate line
# References
# https://press.rebus.community/programmingfundamentals/part/strings-and-files/
# https://www.w3schools.com/python/python_ref_string.asp
# https://stackoverflow.com/questions/22695171/
# print-list-elements-line-by-line-is-it-possible-using-format
# http://www.datasciencemadesimple.com/remove-spaces-in-python/


def get_names():
    print("Enter a list of names seperated by commas")
    raw_names = str(input())
    return raw_names


def split_names(raw_names):
    names = raw_names.split(",")
    return names


def display_names(names):
    for index in names:
        print(index.lstrip().rstrip())


def main():
    raw_names = get_names()
    names = split_names(raw_names)
    display_names(names)


main()

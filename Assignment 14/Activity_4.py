# This program will open "addresses.txt" and reformat an address from three
# lines to one line with comma seperators.
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Files
# https://www.w3schools.com/python/python_file_open.asp
# https://press.rebus.community/programmingfundamentals/


def get_file():
    address_file = open("addresses.txt")
    str = address_file.read()
    split_address = str.split("\n\n")
    address_list = []
    for i in split_address:
        single_address = i.split("\n", 3)
        address_list.append(single_address)
    return address_list
    address_file.close()


def display_addresses(address_list):
    for line in address_list:
        full_name = line[0]
        name = full_name.split(None, 1)
        first_name = name[0]
        last_name = name[1]
        address = line[1]
        last_line = line[2]
        city_rest = last_line.split(",", 1)
        city = city_rest[0]
        rest = city_rest[1]
        state_zip = rest.rsplit(None, 1)
        state = state_zip[0]
        zipcode = state_zip[1]
        print(last_name + ", " + first_name + ", " +
              address + ", " + city + ", " + state + ", " + zipcode)


def main():
    address_list = get_file()
    display_addresses(address_list)


main()

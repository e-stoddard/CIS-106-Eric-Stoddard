# This program will read an xml file and display its' contents along
# with the total number of items and the average price
# References:
# https://stackabuse.com/reading-and-writing-xml-files-in-python/
# https://stackoverflow.com/questions/12040989/printing-all-the-
# values-from-multiple-lists-at-the-same-time
# https://stackoverflow.com/questions/38138699/how-to-find-the-number-
# of-elements-in-element-tree-in-python
# https://stackoverflow.com/questions/7422453/
# python-change-type-of-whole-list
# https://stackoverflow.com/questions/38138699/how-to-find-the-number-of-
# elements-in-element-tree-in-python


def import_xml():
    import xml.etree.ElementTree as ET
    tree = ET.parse("cd_catalog.xml")
    root = tree.getroot()
    return root


def create_title(root):
    title = []
    for elem in root:
        title.append(elem[0].text)
    return title


def create_artist(root):
    artist = []
    for elem in root:
        artist.append(elem[1].text)
    return artist


def create_country(root):
    country = []
    for elem in root:
        country.append(elem[2].text)
    return country


def create_company(root):
    company = []
    for elem in root:
        company.append(elem[3].text)
    return company


def create_price(root):
    price = []
    for elem in root:
        price.append(elem[4].text)
    return price


def create_year(root):
    year = []
    for elem in root:
        year.append(elem[5].text)
    return year


def count_items(root):
    count = len(list(root))
    return count


def convert_price(price):
    price_float = []
    for i in range(len(price)):
        price[i] = float(price[i])
        price_float.append(price[i])
    return price_float


def display_average(price_float, count):
    total = sum(price_float)
    average = total / len(price_float)
    answer = str(round(average, 2))
    print(str(count) + " items - " + "$" + answer + " average price")


def display_contents(title, artist, country, price, year):
    for a, b, c, d, e in zip(title, artist, country, price, year):
        print(str(a) + ", " + str(b) + ", " + str(c) + ", " + str(d) + ", " +
              str(e))


def main():
    root = import_xml()
    title = create_title(root)
    artist = create_artist(root)
    country = create_country(root)
    company = create_company(root)
    price = create_price(root)
    year = create_year(root)
    count = count_items(root)
    price_float = convert_price(price)
    display_contents(title, artist, country, price, year)
    display_average(price_float, count)


main()

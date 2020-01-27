# This program converts the users age in years to the users age in months, weeks, days, hours, minutes and seconds.
print("Enter age in years")
years = int(input())
months = years * 12
weeks = years * 52
days = years * 365
hours = years * 365 * 24
minutes = years * 365 * 24 * 60
seconds = years * 365 * 24 * 60 * 60
print(str(years) + " years old is equal to being; " + str(months) + " months old, " + str(weeks) + " weeks old, " + str(days) + " days old, " + str(hours) + " hours old, " + str(minutes) + " minutes old, " + str(seconds) + " seconds old, ")

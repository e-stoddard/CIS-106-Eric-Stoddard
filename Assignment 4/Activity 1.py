#This program will calculate the users weekly, monthly and annual gross pay

print ("Enter hours worked per week")
hours_week = float(input())

print ("Enter rate per hour")
rate_hour = float(input())

weekly = hours_week * rate_hour
yearly = weekly * 52
monthly = yearly / 12

print ("By working " + str(hours_week) + " hours at a rate of $" +
       str(rate_hour) + " per hour, you will make $" +
       str(weekly) + " per week, $" +
       str(monthly) + " per month and $" +
       str(yearly) + " per year")

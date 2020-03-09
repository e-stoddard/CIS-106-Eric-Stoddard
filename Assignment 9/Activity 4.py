def calculateAnnualPay(weeklyPay):
    annualPay = weeklyPay * 52
    
    return annualPay

def calculateMonthlyPay(annualPay):
    monthlyPay = annualPay / 12
    
    return monthlyPay

def calculateWeeklyPay(hours, hourlyPay):
    weeklyPay = hours * hourlyPay
    
    return weeklyPay

def displayResult(hours, hourlyPay, weeklyPay, monthlyPay, annualPay):
    print("By working " + str(hours) + " hours per week at a rate of $" + str(hourlyPay) + " per hour, you will make $" + str(weeklyPay) + " per week, $" + str(monthlyPay) + " per month, and $" + str(annualPay) + " per year")

def getHourlyPay():
    while True:    #This simulates a Do Loop
        print("Enter Hourly pay")
        hourlyPay = float(input())
        if not(hourlyPay <= 0): break   #Exit loop
    
    return hourlyPay

def getHours():
    while True:    #This simulates a Do Loop
        print("Enter hours worked per week")
        hours = float(input())
        if not(hours <= 0): break   #Exit loop
    
    return hours

# Main
# This program will calculate someones weekly, monthly and annual pay from an hourly rate and hours worked per week.
# References:
# 
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Loops
# 
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Functions
# 
# https://press.rebus.community/programmingfundamentals/
while True:    #This simulates a Do Loop
    hours = getHours()
    hourlyPay = getHourlyPay()
    weeklyPay = calculateWeeklyPay(hours, hourlyPay)
    annualPay = calculateAnnualPay(weeklyPay)
    monthlyPay = calculateMonthlyPay(annualPay)
    displayResult(hours, hourlyPay, weeklyPay, monthlyPay, annualPay)
    print("To run again enter 'Y', to end enter anything except 'Y'")
    rerun = input()
    if not(rerun == "Y" or rerun == "y"): break   #Exit loop
print("Goodbye!")

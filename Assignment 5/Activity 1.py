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
    print("Enter Hourly pay")
    hourlyPay = float(input())
    
    return hourlyPay

def getHours():
    print("Enter hours worked per week")
    hours = float(input())
    
    return hours

# Main
# This program will calculate someones weekly, monthly and annual pay from an hourly rate and hours worked per week.
hours = getHours()
hourlyPay = getHourlyPay()
weeklyPay = calculateWeeklyPay(hours, hourlyPay)
annualPay = calculateAnnualPay(weeklyPay)
monthlyPay = calculateMonthlyPay(annualPay)
displayResult(hours, hourlyPay, weeklyPay, monthlyPay, annualPay)

def calculateDaysOld(yearsOld):
    daysOld = yearsOld * 365
    
    return daysOld

def calculateHoursOld(daysOld):
    hoursOld = daysOld * 24
    
    return hoursOld

def calculateMonthsOld(yearsOld):
    monthsOld = yearsOld * 12
    
    return monthsOld

def calculateSecondsOld(hoursOld):
    secondsOld = hoursOld * 3600
    
    return secondsOld

def displayResult(yearsOld, monthsOld, daysOld, hoursOld, secondsOld):
    print("A person " + str(yearsOld) + " years old is " + str(monthsOld) + " months old, " + str(daysOld) + " days old, " + str(hoursOld) + " hours old and " + str(secondsOld) + " seconds old.")

def getYearsOld():
    print("Enter age in years")
    yearsOld = float(input())
    
    return yearsOld

# Main
# This program will take a persons age in years and calculate a persons age in months, days, hours and seconds
yearsOld = getYearsOld()
monthsOld = calculateMonthsOld(yearsOld)
daysOld = calculateDaysOld(yearsOld)
hoursOld = calculateHoursOld(daysOld)
secondsOld = calculateSecondsOld(hoursOld)
displayResult(yearsOld, monthsOld, daysOld, hoursOld, secondsOld)

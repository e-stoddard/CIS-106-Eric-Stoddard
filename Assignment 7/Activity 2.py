def calculateDays(years):
    days = years * 365
    
    return days

def calculateHours(years):
    hours = years * 8760
    
    return hours

def calculateMonths(years):
    months = years * 12
    
    return months

def calculateSeconds(years):
    seconds = years * 31536000
    
    return seconds

def displayResult(years, result, toScale):
    print(str(years) + " years is equivalent to " + str(result) + toScale)

def getChoice():
    print("Enter M to convert to months, enter D to convert to days, enter H to convert to hours, or enter S to sonvert to seconds", end='', flush=True)
    choice = input()
    
    return choice

def getYears():
    print("Enter age in years")
    years = float(input())
    
    return years

def processDays(years):
    result = calculateDays(years)
    displayResult(years, result, "Days")

def processHours(years):
    result = calculateHours(years)
    displayResult(years, result, "Hours")

def processMonths(years):
    result = calculateMonths(years)
    displayResult(years, result, "Months")

def processSeconds(years):
    result = calculateSeconds(years)
    displayResult(years, result, "Seconds")

# Main
# This program will display a users age in their choice of either months, days, hours or seconds.
# References: https://en.wikiversity.org/wiki/Programming_Fundamentals/Conditions
years = getYears()
choice = getChoice()
if choice == "M" or choice == "m":
    processMonths(years)
else:
    if choice == "D" or choice == "d":
        processDays(years)
    else:
        if choice == "H" or choice == "h":
            processHours(years)
        else:
            if choice == "S" or choice == "s":
                processSeconds(years)
            else:
                print("You muct enter M for months, D for days, H for hours or S for seconds")

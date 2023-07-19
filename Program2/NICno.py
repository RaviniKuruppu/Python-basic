idNumber = input("Enter your ID no.")
year =""
month =""
days=""
numberOfDays=0
gender=""
if(len(idNumber)==10):
    year =idNumber[0:2]
    numberOfDays =(int)(idNumber[2:5])
    
if(len(idNumber)==12):
    year =idNumber[0:4]
    numberOfDays =(int)(idNumber[4:7])
    
if(numberOfDays>500):
        gender = "female"
        numberOfDays = numberOfDays - 500
else:
        gender ="male"
if(numberOfDays<31):
    month ="January"
    days =numberOfDays
elif(numberOfDays<60):
    month ="February"
    days =numberOfDays-31
elif(numberOfDays<91):
    month ="March"
    days =numberOfDays-60
elif(numberOfDays<121):
    month ="April"
    days =numberOfDays-91  
elif(numberOfDays<152):
    month ="May"
    days =numberOfDays-121
elif(numberOfDays<182):
    month ="June"
    days =numberOfDays-152
elif(numberOfDays<214):
    month ="July"
    days =numberOfDays-182
elif(numberOfDays<244):
    month ="August"
    days =numberOfDays-214
elif(numberOfDays<275):
    month ="September"
    days =numberOfDays-244
elif(numberOfDays<305):
    month ="October"
    days =numberOfDays-275
elif(numberOfDays<335):
    month ="November"
    days =numberOfDays-305
elif(numberOfDays<365):
    month ="December"
    days =numberOfDays-335
print("birth year ",year)
print("Month ",month)
print("Day ",days)
print("gender "+gender)









newId ="196410402750"
newLength =len(newId)

oldId="840983277v"
oldLength =len(oldId)






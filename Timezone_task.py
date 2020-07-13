from datetime import datetime as date
import calendar
currentDate=date.now()
currentTime = currentDate.strftime("%H:%M:%S")
dateInput=input("Enter the input:")
n1= dateInput.split(' ')
print(n1)
if n1[3] <= currentTime<= n1[4]:
    print("true")
elif currentTime<n1[3]:
    print(n1[3])
else:
    print("False")

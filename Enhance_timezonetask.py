from datetime import datetime as date
import calendar
TW = date.today().strftime("%A")
current_date = date.now()
currentTime = current_date.strftime("%H:%M:%S")
dateInput = input("Enter the input:")
n1 = dateInput.split(' ')
if n1[8] == TW or n1[10] == TW and n1[6] <= currentTime <= n1[7]:
    print('True')
elif n1[8] != TW and n1[10] != TW:
    print(n1[8], n1[6])
elif n1[8] == 'Sunday' and n1[10] == 'Tuesday' and TW == 'Monday':
    print(n1[10], n1[6])
elif n1[8] == 'Monday' and n1[10] == 'Wednesday' and TW == 'Tuesday':
    print('Wednesday', n1[6])
elif n1[8] == 'Tuesday' and n1[10] == 'Thursday' and TW == 'Wednesday':
    print(n1[10], n1[6])
elif n1[8] == 'Wednesday' and n1[10] == 'Friday' and TW == 'Thursday':
    print(n1[10], n1[6])
elif n1[8] == 'Thursday' and n1[10] == 'Saturday' and TW == 'Friday':
    print(n1[10], n1[6])
elif n1[8] == 'Friday' and n1[10] == 'Sunday' and TW == 'Saturday':
    print(n1[10], n1[6])
elif n1[8] == 'Saturday' and n1[10] == 'Monday' and TW == 'Sunday':
    print(n1[10], n1[6])


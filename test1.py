file_path ="C:/Users/Pc1/Desktop/Python/date.txt"

import datetime

current_date = datetime.datetime.now()
print(current_date)
print("Year:" ,current_date.year)
print("Year:" ,current_date.month)
print("Year:" ,current_date.day)
print("Year:" ,current_date.hour)
print("Year:" ,current_date.minute)
print("Year:" ,current_date.second)
print("Year:" ,current_date.microsecond)


current_date1 = datetime.datetime.now().time()
print(current_date1)
current_date2 = datetime.datetime.now().date()
print(current_date2)

time_object = datetime.time(12,30,41,1024)
print(time_object)
date_object = datetime.date(2025,4,15)
print(date_object)

duration = datetime.timedelta(days = 5, hours = 2)
print(duration)
math = current_date - duration
print(math)


birthday = datetime.timedelta(days = 5667)
print(birthday)

birth_date = current_date - birthday
print(birth_date)

with open(file_path, "w")as file:
    file.write((f"{current_date}"))
    file.write((f"{birth_date}"))


import datetime
current_datetime = datetime.datetime.now()

print(current_datetime)
print("Year:" ,current_datetime.year)
print("Month:" ,current_datetime.month)
print("Day:" ,current_datetime.day)
print("Hour:" ,current_datetime.hour)
print("Minute:" ,current_datetime.minute)
print("Second:" ,current_datetime.second)
print("Microsecond:" ,current_datetime.microsecond)


current_datetime1 = datetime.datetime.now().date()
print(current_datetime1)
current_datetime2 = datetime.datetime.now().time()
print(current_datetime2)

time_objekt = datetime.time(12,30,45,12034)
print(time_objekt)
time_objekt2 = datetime.date(2025,5,13)
print(time_objekt2)

duration = datetime.timedelta(days=5,hours=3)
print(duration)

new_data = current_datetime + duration 
print(new_data)

birthday = datetime.timedelta(days=5900)
prev_date = current_datetime - birthday
print(prev_date)
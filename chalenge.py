file_path = "C:/Users/Student/Desktop/lesson11/txtdata.txt"
import datetime
current_date = datetime.datetime.now()
print(current_date)
duration = datetime.timedelta(days=100)
print(duration)

new_date = current_date + duration 
print(new_date)

old_date = datetime.timedelta(days=100)
previous_date = current_date - old_date
print(previous_date)

with open(file_path, "w")as file:
    file.write((f"{new_date}"))
    file.write((f"{old_date}"))
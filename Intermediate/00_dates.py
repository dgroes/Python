# Datos
from datetime import datetime

now = datetime.now()

print(now)
print(now.year)
print(now.day)
print(now.minute)
print(now.second)
print(now.year)
print(now.month)

timestamp = now.timestamp()
print(timestamp)

print("--------------")
# Minimo el año, mes y día
year_2026 = datetime(2026, 1, 1, 3)
print(year_2026)

print("-------------")


def print_date(date):
    print(date)
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(year_2026)

print("--------------")
from datetime import time

current_time = time(21, 6, 0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print("--------------")

from datetime import date

# Utilización de today()
current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

# Fecha de forma manual
current_date = date(2027, 9, 4)
print(current_date.year)
print(current_date.month)
print(current_date.day)

print("--------------")
# Operaciones con fechas
current_date = date(current_date.year + 10, current_date.month + 2, current_date.day)
print(current_date.year)

print("--------------")
# OPeraciones solo que posean el mismo formato, en este caso datetime.datetime
diff = year_2026 - now
print(diff)
# print(year_2026 - current_date)

print("--------------")
from datetime import timedelta
# time_delta = time_delta
start_timedelta = timedelta(200, 100,1000, weeks= 30)
end_timedelta = timedelta(300, 500, 2000, weeks=33)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
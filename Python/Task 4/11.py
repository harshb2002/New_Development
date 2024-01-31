from datetime import datetime
import calendar

today = datetime.now()

first_day = today.replace(day=1)

_, last_day = calendar.monthrange(today.year, today.month)
last_day = today.replace(day=last_day)

print(f"First date of the current month: {first_day.strftime('%dth %B %Y %A %I:%M:%S %p')}")
print(f"Last date of the current month: {last_day.strftime('%dth %B %Y %A %I:%M:%S %p')}")

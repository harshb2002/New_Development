from datetime import datetime
import calendar

today = datetime.now()

first_day = today.replace(day=1)

_, last_day = calendar.monthrange(today.year, today.month)
last_day = today.replace(day=last_day)

# Print the result
print(f"First date of the current month: {first_day.strftime('%Y-%m-%d')}")
print(f"Last date of the current month: {last_day.strftime('%Y-%m-%d')}")

from datetime import datetime

# x = datetime.datetime(2024,2,20)
x = datetime.now()

first_day = x.replace(day=1)

print(f"Today's day: {x.strftime('%A')}")
print(f"First day of the current month: {first_day.strftime('%A')}")

from datetime import datetime

# x = datetime.datetime(2024,2,20)
x = datetime.now()

first_day = x.replace(month=1,day=1)

print(f"Today's day: {x.strftime('%A')}")
print(f"First month of the current year: {first_day.strftime('%B')}")

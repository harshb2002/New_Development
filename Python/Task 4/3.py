from datetime import datetime

# a = datetime.datetime(2024,1,22)
# b = datetime.datetime(2023,1,22)

# date_diff = abs(a - b)

# diff_in_days = date_diff.days
# print(diff_in_days)


x = input("Enter the first date (YYYY-MM-DD): ")
y = input("Enter the second date (YYYY-MM-DD): ")

date_format = "%Y-%m-%d"  # Adjust the format based on your input date format
date1 = datetime.strptime(x, date_format)
date2 = datetime.strptime(y, date_format)

date_diff = abs(date2 - date1)

diff_in_days = date_diff.days

print(f"The difference between the two dates is {diff_in_days} days.")

from datetime import datetime , timedelta

x = datetime.now()

new_date = x + timedelta(days=7)

print(f"Today's Date is : {x}")
print(f"Date after one week from today is : {new_date}")
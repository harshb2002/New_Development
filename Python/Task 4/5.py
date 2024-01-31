from datetime import datetime 
from dateutil.relativedelta import relativedelta

x = datetime.now()

new_date = x + relativedelta(years=1)

print(f"Today's Date is : {x}")
print(f"Date after one week from today is : {new_date}")
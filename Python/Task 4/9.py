from datetime import datetime, timedelta
import calendar

def get_week_dates_for_current_month():
    today = datetime.now()
    first_day_of_month = today.replace(day=1)
    
    _, last_day_of_month = calendar.monthrange(today.year, today.month)

    days_to_add = (first_day_of_month.weekday() - calendar.MONDAY) % 7

    start_date = first_day_of_month - timedelta(days=days_to_add)

    week_dates = []

    for i in range(7):
        current_date = start_date + timedelta(days=i)
        if current_date.month == today.month:
            week_dates.append(current_date)

    return week_dates

week_dates = get_week_dates_for_current_month()

for date in week_dates:
    print(date.strftime('%Y-%m-%d'))

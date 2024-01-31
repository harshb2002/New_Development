from datetime import datetime

def calculate_age(birthdate):
    current_date = datetime.now()

    age_difference = current_date - birthdate

    age_years = age_difference.days // 365
    age_months = (age_difference.days % 365) // 30
    age_days = (age_difference.days % 365) % 30

    return age_years, age_months, age_days

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

age_years, age_months, age_days = calculate_age(birthdate)

print(f"Your age is: {age_years} years, {age_months} months, and {age_days} days.")

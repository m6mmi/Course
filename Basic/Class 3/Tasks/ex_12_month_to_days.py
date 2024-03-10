import calendar

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_nr = 0

user_input_year = int(input("Enter year: "))
for i in months:
    print(i, end=", ")
print()

user_input_month = input("Enter month (string): ").lower()


for month in months:
    month_nr += 1
    if user_input_month == month.lower():
        days = calendar.monthrange(user_input_year, month_nr)[1]
        print(f"In {month} of {user_input_year} is {days} days")

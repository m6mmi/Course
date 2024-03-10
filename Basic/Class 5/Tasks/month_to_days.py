months_dict = {"January": 31,
               "February": 29,
               "March": 31,
               "April": 30,
               "May": 31,
               "June": 30,
               "July": 31,
               "August": 30,
               "September": 30,
               "October": 30,
               "November": 31,
               "December": 31
               }

user_month = input("What is the month name you want to know the amount of days to: ").lower()
print(f"The amount of days in {user_month} is {months_dict[user_month]}")
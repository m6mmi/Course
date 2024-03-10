year = int(input("Enter the year: "))

if year < 1:
    print("Nice! You are not even in a first century yet!")
else:
    print(f"You are in the {((year - 1) // 100) + 1} century")


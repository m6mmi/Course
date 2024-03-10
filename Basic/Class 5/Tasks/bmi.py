print("BMI calculator")
height = float(input("Enter height (meters): "))
weight = float(input("Enter weight (kilograms): "))

bmi = round(weight/(height ** 2), 2)

if 0 < bmi <= 18.5:
    result = "Underweight"
elif bmi <= 25.0:
    result = "Normal"
elif bmi <= 30.0:
    result = "Overweight"
elif bmi > 30:
    result = "Obese"
else:
    print("Something went wrong !!!")

print(f"Your BMI is {bmi} = {result}")
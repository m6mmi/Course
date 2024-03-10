import sys

dog_year = int(sys.argv[1])

# dog_year = int(input("How old dog is: "))


if dog_year <= 2:
    human_years = dog_year * 10.5
else:
    human_years = 21+(dog_year-2)*4

print(f"{dog_year} dog years is {human_years} human years")
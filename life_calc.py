#Calculating amount life left if you live to 90 years old
age = input("What is your current age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = age_as_int * 365
weeks_remainng = age_as_int * 52
months_remaining = age_as_int * 12

message = f"You have {days_remaining} days, {weeks_remainng} weeks, {years_remaining} years"

print(message)

age = input("What is your current age? ")


# age_as_int = int(age) # Another way we could have defined age to be Integer

years_left = 90 - int(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12



print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")



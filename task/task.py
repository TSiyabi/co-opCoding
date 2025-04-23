name = input("What's your name? ")
age = int(input("How old are you? "))

import datetime

current_year = datetime.datetime.now().year
year_hundred = current_year + (100 - age)

print(f"Hello, {name}!")
print(f"You will turn 100 years old in the year {year_hundred}.")
print("Have a great day!")

a = input("Enter ur address: ")
print(a)
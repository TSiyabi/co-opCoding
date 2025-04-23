import datetime
name = input("What's your name? ")
age = int(input("How old are you? "))
country = input("what is your country of origin? ")
status = input("single or married")
address = input("Enter ur address: ")
skills = input("Kindly list your key skills (separated by commas): ")
skill_list = [skill.strip() for skill in skills.split(',')]

password = input("give me the password please\n3 chances before the most wanted hitman shoots you in the head\nand replaces you with a skin walker\ngood luck:")
print(address)


print(f"Hello, {name}!")

print("\nThank you for sharing your skills.")
print("hello world Have a great day!")
print("OOOO")
print("your status is" + status)
print("OOOO")
print("your country of origin is " + country)
print(password)
current_year = datetime.datetime.now().year
year_hundred = current_year + (100 - age)
print(f"You will turn 100 years old in the year {year_hundred}.")
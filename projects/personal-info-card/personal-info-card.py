# Personal Info Card v1
# Day 2 — May 25, 2026
# Built with: input, print, f-strings, string concatenation
# 
# TODO v2 (after learning loops + exceptions):
# - Add input validation for age (must be positive integer)
# - Add empty field validation
# - Better alignment with .ljust()

name = input("What's your name? ")
name = name.strip().title()

age = input("What's your age? ").strip()
age = int(age)

occupation = input("What's your occupation? ")
occupation = occupation.strip().title()

location = input("What's your location? ")
location = location.strip()

display_name = name if name != "" else "Unknown"
display_age = age if age > 0 else "Unknown"
display_occupation = occupation if occupation != "" else "Unknown"
display_location = location if location != "" else "Unknown"

print("+" + "-" * 30 + "+")
print(f"Name: {display_name}")
print(f"Age: {display_age}")
print(f"Occupation: {display_occupation}")
print(f"Location: {display_location}")
print("+" + "-" * 30 + "+")
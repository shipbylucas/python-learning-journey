# Personal Info Card v2
# Day 8 — May 30, 2026
# Built with: functions, try/except, while loops, input validation

def main():
    name = get_name()
    age = get_age()
    occupation = get_occupation()
    location = get_location()
    display_info(name, age, occupation, location)

def get_name():
    while True:
        name = input("What's your name? ")
        name = name.strip().title()
        if name != "":
            break
        else:
            print("Name cannot be empty. Try again.")
    return name

def get_age():
    while True:
        try:
            age = input("What's your age? ")
            age = int(age)
            if 1 <= age <= 120:
                break
            else:
                print("Age must be between 1 and 120. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number. Try again.")
    return age

def get_occupation():
    while True:
        occupation = input("What's your occupation? ")
        occupation = occupation.strip().title()
        if occupation != "":
            break
        else:
            print("Job cannot be empty. Try again.")
    return occupation
    
def get_location():
    while True:
        location = input("What's your location? ")
        location = location.strip().title()
        if location != "":
            break
        else:
            print("Location cannot be empty. Try again.")
    return location

def display_info(name, age, occupation, location):
    print("+" + "-" * 30 + "+")
    print("PERSONAL INFO CARD".center(30))
    print("+" + "-" * 30 + "+")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Occupation: {occupation}")
    print(f"Location: {location}")
    print("+" + "-" * 30 + "+")

main()

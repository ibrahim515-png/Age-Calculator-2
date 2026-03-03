# Age Calculator - Beginner Version
# By: Ibrahim Salah

current_year = 2025  # Current year

# Ask the user to enter their birth year
birth_year = int(input("Enter your birth year: "))

# Calculate age
age = current_year - birth_year

# Validate input
if age < 0:
    print("Invalid birth year.")
else:
    print("Your age is:", age, "years")

    # Age category message
    if age < 18:
        print("You are a minor.")
    elif age <= 60:
        print("You are an adult.")
    else:
        print("You are a senior.")

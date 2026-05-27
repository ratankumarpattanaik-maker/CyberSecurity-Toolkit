import re

print("=== Password Strength Checker ===")

password = input("Enter Password: ")

strength = "Weak"

if (len(password) >= 8 and
    re.search("[A-Z]", password) and
    re.search("[a-z]", password) and
    re.search("[0-9]", password) and
    re.search("[@#$%^&*!]", password)):

    strength = "Strong"

print("\nPassword Strength:", strength)

if len(password) < 8:
    print("- Password should contain at least 8 characters")

if not re.search("[A-Z]", password):
    print("- Add at least one uppercase letter")

if not re.search("[a-z]", password):
    print("- Add at least one lowercase letter")

if not re.search("[0-9]", password):
    print("- Add at least one number")

if not re.search("[@#$%^&*!]", password):
    print("- Add at least one special character (@#$%^&*!)")
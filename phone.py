
import re

phone = input("Enter your phone number: ")

if re.fullmatch(r"[0-9]{10}", phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

# import sys
# import os

# PyInto Lesson 05
# Strings
# - Functions
# - Input from terminal
# - Formatted Strings

name = "NIKOLA TESLA"
quote = "The only mystery in life is: why did Kamikaze pilots wear helmets?"

print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title())

print(name.isalpha())

print(quote.find('Kamikaze'))
print(quote.find('Kamikazsdfe'))

new_name = input("Please enter a name: ")
print(new_name)

print(len(quote))

print(f"Hello {new_name}, you owe me 1 million dollars!")

print(f"{quote.strip('?')}")
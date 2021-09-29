"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9.0
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


while choice != "Q":
    if choice == "C":
        celsius = float(input("celsius: "))
        print(celsius_to_fahrenheit(celsius))
    elif choice == "F":
        fahrenheit = float(input("fahrenheit: "))
        print(fahrenheit_to_celsius(fahrenheit))
    else:
        print("Invalid option")
print("Thank you.")

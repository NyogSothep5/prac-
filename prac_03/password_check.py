"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2


def main():
    print("Please enter a valid password")
    print("Your password must be longer than", MIN_LENGTH)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")


def is_valid_password(password):
    if len(password) < MIN_LENGTH:
        return False
    else:
        n = int(len(password))
        for i in range(n):
            print('*', end="")
    return True


main()

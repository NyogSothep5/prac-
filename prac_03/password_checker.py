"""0
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    password = get_password()
    print_star(password)
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password), password))


def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    elif password.isdigit():
        print("缺少字母")
    elif password.isalpha():
        print("缺少数字")
    elif password.islower():
        print("缺少大写字母")
    elif password.isupper():
        print("缺少小写字母")
    else:
        print("设置密码成功")
    return True


def get_password():
    password = input("> ")
    return password


def print_star(password):
    length = len(password)
    for i in range(length):
        print('*', end="")


main()

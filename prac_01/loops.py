MENU = """0 - Displays all of the odd numbers between 1 and 20.
A - Count in 10s from 0 to 100.
B - Count down from 20 to 1.
C - Print n stars.
D - Print n lines of increasing stars.
Q - Quit."""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "0":
        for i in range(1, 21, 2):
            print(i, end=' ')
        print()
    elif choice == "A":
        for i in range(0, 100, 10):
            print(i, end=' ')
        print()
    elif choice == "B":
        for i in range(20, 1):
            print(i, end=' ')
        print()
    elif choice == "C":
        n = int(input("Enter Number of stars: "))
        for i in range(n):
            print('*', end="")
        print()
    elif choice == "D":
        n = int(input("Enter Number of stars: "))
        for i in range(n+1):
            print('*' * n)
        print()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
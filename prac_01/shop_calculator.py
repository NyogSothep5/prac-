n = int(input("Number of items: "))
a = 0
for i in range(n):
    a = a + float(input("Price of item: $"))
    if a <= 0:
        print("Invalid number of items!")
while a >= 100:
    a = a * 0.9
    break
print("Total price for 3 items is ${:.2f}".format(a))
FILENAME = "name.txt"
name = input("Enter name: ")
print(name, file=out_file)
out_file.close()

out_file=open("name.txt")
print("Your name is {}".format(name))
out_file.close()

total=0
in_file=open("number", "r")
for i in range(2):
    text = in_file.readline()
    total = total +int(text)
print("The total is: ", total)
in_file.close()
# Name : Shubham Sapkal # Roll No. : 2012118

# Write a python program to read three numbers and find the smallest among them

n1 = int(input("Enter the 1st number: "))

n2 = int(input("Enter the 2nd number: "))

n3 = int(input("Enter the 3rd number: "))


if (n1 < n2):
    if (n1 < n3):
        print("N1 is the smallest number")
    else:
        print("N3 is the smallest number")
elif (n2 < n3):
    print("N2 is the smallest number")
else: print("N3 is the smallest number")
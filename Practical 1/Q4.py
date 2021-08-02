# Name : Shubham Sapkal # Roll No. : 2012118

# Write a python program to read three numbers and if any two variables are equal, print that number

n1 = int(input("Enter the 1st number: "))

n2 = int(input("Enter the 2nd number: "))

n3 = int(input("Enter the 3rd number: "))


if (n1 == n2):
    print("N1 and N2 variables are equal")
elif (n2 == n3):
    print("N2 and N3 variables are equal")
elif (n1 == n3):
    print("N1 and N3 variables are equal")
else:
    print("variables are not equal")

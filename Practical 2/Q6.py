# Name : Shubham Sapkal # Roll No. : 2012118

# Write a python program to read three numbers and print them in ascending order (without using sort function)

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if x > y:
    x,y = y,x
if x > z:
    x,z = z,x
if y > z:
    y,z = z,y

# Ascending order!

print (x, "->", y, "->", z)



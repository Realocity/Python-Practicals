# Name : Shubham Sapkal Roll No. : 2012118
# Write a Python program to read first n lines of a file.

n = 3
file = open('test.txt')
for i in range(n):
    print(file.readline())
file.close()
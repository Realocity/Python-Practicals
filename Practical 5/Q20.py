# Name : Shubham Sapkal Roll No. : 2012118
# Write a Python program to copy the contents of a file to another file.

file = open('test.txt')
file2 = open('test2.txt', 'a')
file2.write(file.read())
file.close()
print("Data Copied to test2 File...")
file2.close()
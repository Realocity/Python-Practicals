# Name : Shubham Sapkal Roll No. : 2012118
# Write a Python program to count the number of lines in a text file.

with open('test.txt') as file:
    print('The Total Number of lines in text file : ')
    print(len(list((file))))
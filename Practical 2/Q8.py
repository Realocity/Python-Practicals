# Name : Shubham Sapkal # Roll No. : 2012118

# Write a python program to read a number, 
# if it is an even number, 
# print the square of that number and if it is odd number print cube of that number.

read = int(input('Enter the value : '))

if(read % 2 == 0):
     print(f'The square of {(read)} is {(read**2)}')
else:
     print(f'The cube of {(read)} is {(read**3)}')
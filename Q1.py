# Name : Shubham Sapkal # Roll No. : 2012118

# Python program to swap two variables using third variable.

# inputs from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
swap = x
x = y
y = swap

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
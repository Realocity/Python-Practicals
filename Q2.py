# Write a python program to swap two numbers without using third variable

x = input('Enter value of x: ')
y = input('Enter value of y: ')
 
print ("The value of x before swapping:", x)
print ("The value of y before swapping:", y)
 
# No need of temporary variable
# swap the values
 
x, y = y, x
 
print ("The value of x after swapping:", x)
print ("The value of y after swapping:", y)
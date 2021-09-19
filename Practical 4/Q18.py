# Name : Shubham Sapkal Roll No. : 2012118
# Write a Python script to display the various Date Time formats.

'''
a) Current date and time 
b) Current year 
c) Month of year 
d) Week number of the year 
e) Weekday of the week 
f) Day of year 
g) Day of the month 
h) Day of week

'''
import datetime

print(f'Current date and time : {datetime.datetime.now()}')
print(f'Current year : {datetime.date.today().year}')
print(f'Current Month of year : {datetime.date.today().month} that is {datetime.date.today().strftime("%B")}')
print(f'Current Week number of the year : {datetime.date.today().isocalendar()[1]}')
print(f'Current Weekday of the week : {datetime.date.today().isoweekday()}')   
print(f'Current Day of year : {datetime.date.today().strftime("%j")}')
print(f'Current Day of the month : {datetime.date.today().strftime("%d")}')
print(f'Current Day of week : {datetime.date.today().strftime("%A")}')
# Program to display calendar of the given month and year

import calendar

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

print(calendar.month(yy, mm))

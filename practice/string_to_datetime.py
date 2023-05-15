# Python program to convert string to datetime

# # method 1

# from datetime import datetime

# my_date_string = "Mar 11 2011 11:31AM"

# datetime_object = datetime.strptime(my_date_string, "%b %d %Y %I:%M%p")

# print(type(datetime_object))
# print(datetime_object)


# method 2

from dateutil import parser

date_time = parser.parse("Mar 11 2011 11:31AM")

print(date_time)
print(type(date_time))
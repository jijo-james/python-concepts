# Python program to represent enum


from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3

print(Day.MONDAY)

print(Day.MONDAY.name)

print(Day.MONDAY.value)
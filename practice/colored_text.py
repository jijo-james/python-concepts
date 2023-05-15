# Python program to print colored text to the terminal

# # method 1

# print("\x1b[38;2;5;86;243m" + "Programiz" + "\x1b[0m")


#method 2

from termcolor import colored

print(colored('Programiz', 'blue'))
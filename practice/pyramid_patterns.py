# # Problem 1: Program to print half pyramid using *

# rows = int(input("Enter number of rows: "))

# for i in range(rows):
#     for j in range(i+1):
#         print("* ", end="")
#     print("\n")


# # Problem 1: Program to print half pyramid using numbers

# rows = int(input("Enter number of rows: "))

# for i in range(rows):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print("\n")


# Problem 1: Program to print half pyramid using alphabets

rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i + 1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")

    ascii_value += 1
    print("\n")
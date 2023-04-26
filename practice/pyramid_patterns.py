# # Problem 1: Program to print half pyramid using *

# rows = int(input("Enter number of rows: "))

# for i in range(rows):
#     for j in range(i+1):
#         print("* ", end="")
#     print("\n")


# # Problem 2: Program to print half pyramid using numbers

# rows = int(input("Enter number of rows: "))

# for i in range(rows):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print("\n")


# # Problem 3: Program to print half pyramid using alphabets

# rows = int(input("Enter number of rows: "))

# ascii_value = 65

# for i in range(rows):
#     for j in range(i + 1):
#         alphabet = chr(ascii_value)
#         print(alphabet, end=" ")

#     ascii_value += 1
#     print("\n")


# # Problem 4: Program to print inverted half pyramid using *

# rows = int(input("Enter number of rows: "))

# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print("* ", end=" ")
    
#     print("\n")


# Problem 5: Program to print inverted half pyramid using numbers

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    
    print("\n")
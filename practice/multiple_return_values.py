# Python program to return multiple values from a function


# method1
def name():
    return "Jijo", "James"


print(name())

name_1, name_2 = name()
print("first name: ", name_1, "\n", "second name: ", name_2)

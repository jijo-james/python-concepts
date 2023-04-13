my_list = [12, 65, 54, 39, 102, 339, 221,]

number = int(input("Enter the number: "))
# use anonymous function to filter
result = list(filter(lambda x: (x % number == 0), my_list))

# display the result
print("Numbers divisible by 13 are",result)

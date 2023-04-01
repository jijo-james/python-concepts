count = 0
for year in range(2023):
    
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year)
        count += 1
print(count)





# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x**2, numbers))
# print(squared_numbers)
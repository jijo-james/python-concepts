numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = map(lambda n : n*n, numbers)
# it creates a map object, either iterate through it
# or get each next element with 'next' fn
# or convert it to a list using 'list()' function

# my_list = [ n*n for n in numbers]

# my_list = [n for n in numbers if n%2 ==0]

my_list = list(filter(lambda n: n%2 == 0, numbers))

print(my_list)

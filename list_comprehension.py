nums = [1,2,3,4,5,6,7,8,9,10]

# my_list = map(lambda n : n*n, nums)

# my_list = [ n*n for n in nums]

my_list = [n for n in nums if n%2 ==0]

print (my_list)
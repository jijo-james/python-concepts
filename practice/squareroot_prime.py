original_list = [1,4,9,16,25,36,49,56]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int((num**.5)+1)):
        if num % i == 0:
            print(num)
            return False
    return True

# simple method
new_list = []

for num in original_list:
    sqrt_num = num**.5
    if is_prime(sqrt_num):
        new_list.append(num)


# using list comprehension

# new_list = [num for num in original_list if is_prime(num**.5)]

print(new_list)
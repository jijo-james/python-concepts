# 1

# def myfunc(n):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("\r")


# n = 5
# myfunc(n)


# 2


# def myfunc(n):
#     k = n - 1
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("\r")


# n = 5
# myfunc(n)


# 3


# def num(n):
#     num = 1
#     for i in range(0, n):
#         num = 1
#         for j in range(0, i + 1):
#             print(num, end=" ")
#             num = num + 1
#         print("\r")


# n = 5
# num(n)


# 4


# def num(n):
#     num = 1
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print(num, end=" ")
#             num = num + 1
#         print("\r")


# n = 5
# num(n)


# def sum_of_elements(nums):
#     return sum(nums)


# num = [1, 2, 3, 4, 5]
# print(sum(num))


# def find_first_index(nums, target):
#     return nums.index(target)


# print(find_first_index([1, 2, 3, 4, 5], 2))


n = [1, 2, 3, 4, 5]
# print(list(reversed(n)))

# my_list = ["hello", "world"]
# new_string = ""
# for x in my_list:
#     new_string += x + " "

# print(new_string.strip())


# y = [(lambda x: x * x)(x) for x in n]
# print(y)


# animals = ["cat", "dog", "rabbit", "horse"]


# def search(list_name: list, element):
#     if element in animals:
#         return list_name.index(element)
#     else:
#         return False


# print(search(animals, "hose"))


import time


# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True


# def find_primes_in_range(start, end):
#     primes = []
#     for num in range(start, end + 1):
#         if is_prime(num):
#             primes.append(num)
#     return primes


# Python program to display all the prime numbers within an interval

# lower = 900
# upper = 1000

# print("Prime numbers between", lower, "and", upper, "are:")


def find_primes_in_range(lower, upper):
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                pass


# Example usage:
start_num = 10
end_num = 100000
start_time = time.time()
prime_numbers = find_primes_in_range(start_num, end_num)
end_time = time.time()

execution_time = end_time - start_time
# print(f"Prime numbers between {start_num} and {end_num} are: {prime_numbers}")
print(f"Total execution time: {execution_time} seconds.")

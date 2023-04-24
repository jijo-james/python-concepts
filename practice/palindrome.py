my_str = input("Enter a string: ").casefold()

rev_str = reversed(my_str)


if list(my_str) == list(rev_str):
    print("String is PALINDROME...")
else:
    print("Not PALINDROME!!!")

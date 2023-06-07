# Python program to check two strings are anagram


string_1 = "Jijo"
string_2 = "joji"

string_1 = string_1.lower()
string_2 = string_2.lower()

if len(string_1) == len(string_2):
    sorted_1 = sorted(string_1)
    sorted_2 = sorted(string_2)

    if sorted_1 == sorted_2:
        print("Anagram")
    else:
        print("Not Anagram")

else:
    print("Not Anagram")

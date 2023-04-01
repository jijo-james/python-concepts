def compress_string(s):
    result = ""
    count = 1
    prev = s[0]
    for c in s[1:]:
        if c == prev:
            count += 1
        else:
            result += str(count) + prev
            count = 1
            prev = c
    result += str(count) + prev
    return result

# Example usage
input_str = "AA"
output_str = compress_string(input_str)
print(output_str)

# test_cases
# 1 AAAABBCCCDAA
# 2 AAAAA
# 3 ABCD
# 4 AADDDDDD
# 5 A
# 6 ABCDABBC

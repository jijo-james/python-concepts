# Python program to iterate over dictonaries

# # method 1
# dt = {"a": "juice", "b": "grill", "c": "corn"}

# for key, value in dt.items():
#     print(key, value)

# # method 2
# dt = {"a": "juice", "b": "grill", "c": "corn"}

# for key in dt:
#     print(key, dt[key])

# # method 3
# dt = {"a": "juice", "b": "grill", "c": "corn"}

# for key, value in dt.iteritems():
#     print(key, value)

# method 4
dt = {"a": "juice", "b": "grill", "c": "corn"}

for key in dt.keys():
    print(key)

for value in dt.values():
    print(value)

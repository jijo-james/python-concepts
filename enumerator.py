
'''
#instead of this
names = ['Jijo', 'Adharsh', 'Sajjad']
index = 0
for name in names:
    index += 1
    print(index, name)
'''

#use this
names = ['Jijo', 'Adharsh', 'Sajjad']
for index, name in enumerate(names, start=1):
    print(index, name)
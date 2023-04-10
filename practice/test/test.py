# class HelloPython:
#     def __init__(self, name: str) -> None:
#         self.name = name

def hello( name):
        
    print("Hello World, {}".format(name))

# hp = HelloPython()
if __name__ == '__main__':
    user_name = input("Enter your name: ")
    hello(user_name)










# valid = True
# while valid == True:
#     count = input("Enter the number count: ")
    
#     try:
#         if int(count):
#             valid = False
#     except:
        
#         print("Please enter a valid number")
#         continue
    

# numbers = []

# for i in range(int(count)):
#     number = int(input("Enter the {}th number: ".format(i+1)))
#     numbers.append(number)

# max = numbers[0]
# for n in numbers:
#     if n > max:
#         max = n

# print(max)
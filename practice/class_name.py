# Python program to get the class name of an instance


# # method 1
# class Vehicle:
#     def name(self, name):
#         return name

# v = Vehicle()
# print(v.__class__.__name__)


# method 2
class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(type(v).__name__)
# # p = W/t
# # S = D/t
 
# # Distance is always positive
# # S>1 then calculate power
# # S<0 then throw exception and cal power
 
# # format
# # 'company' : [distance, time, work]
 
# car = {         
# 'BMW' : [25, 40, 200],
# 'MB' : [50, 20, 400],
# 'AUDI' : [40, 30.5, 320],
# 'LAM' : [-40, 30.5, 320]
# }

# # print(type(car.values()))


# class Cars():

#     def __init__(self):
#         return
    
#     def calculations(self, car):
#         for key, value in car.items():
#             try:
#                 if value[0] > 0:
#                     speed = value[0]/value[1]
#                     print(speed)
                
#                     if speed > 1:
#                         power = value[2]/value[1]
#                     try:
#                         if 0 < speed <1:
#                             pass
#                     except:
#                         print("Speed is {}, which is < 0".format(speed))
#                         power = value[2]/value[1]
#             except:
#                 print("Distance is , which is a negative value")
            
#             print( speed, power)


# c = Cars()

# c.calculations(car)

import sys

print(sys.getsizeof(dict()))
print(sys.getsizeof(list()))
print(sys.getsizeof(tuple()))
print(sys.getsizeof(int()))
print(sys.getsizeof(str()))


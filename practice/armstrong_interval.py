# Program to check Armstrong numbers in a certain interval

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

if lower > upper:
    print("Lower limit must be less than upper limit...!!!")

else:
    for num in range(lower, upper + 1):

        # order of number
        order = len(str(num))
            
        # initialize sum
        sum = 0

        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print(num)

# We can take input in python with the help of input() function

a = input("Enter your name: ")      # By default all the values are considered to be of string type, therefore we need to typecast some times...
print("Your name is: " +a)

num = input("Enter a number: ")
print(type(num))                    # The data type of 'num' will be string even if we enter a number so we need to typecast it into integer

num1 = int(input("Enter a number: "))
print(type(num1))
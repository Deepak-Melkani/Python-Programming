def add(a, b):
    return a + b

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
sum = add(a, b)
print("The addition of a and b is: ",sum)

def table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

num = int(input("Enter the number you want to print the table of: "))
table(num)
table(7)
table(19)
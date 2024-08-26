num = int(input("Enter a number: "))

print(f'The table of {num} is...')

for i in range(1, 11):
    print(f'{num} x {i} = {num*i}')

for i in range(51):
    print(i)


a = 7
while(a > 0):
    print(a)
    a -= 1

for i in range(45):
    pass                # The pass keyword is used to skip the loop

list = [1,2,3,4,5,6,7,8,9,10]

for item in list:
    print(item)
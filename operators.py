a = 18
b = 7

# Opeartors +,  -,  *,  / comes under the category of Arithmetic operators...

print(f"The addition of a and b is: {a+b}")                 # + is an arithmetic operator applied on variables a and b
print(f"The multiplication of a and b is: {a*b}")           # * is an arithmetic operator applied on variables a and b
print(f"a raised to power 3 is: {a**3}")


# Opeartors =,  +=,  -=,  *=,  /=  comes under the category of Assignment operators...

a *= 5              # This means a = a * 5 (similar is the functionality of other operators too..)
print(a)


# Operators ==,  <,  <=,  >,  >=  comes under the category of Relational operators...

if(a > b):
    print("a is greater than b")

else:
    print("b is greater than a")



# Operators 'and', 'or', 'not' fall under the category of Logical operators

voterCardIsued = True 
if(a >=18 and voterCardIsued):
    print("You are eligible to vote")
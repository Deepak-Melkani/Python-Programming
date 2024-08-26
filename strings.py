# Can be enclosed within single, double or triple quotes
# Slicing can be done in order to get a part of the string 
# Strings are immutable

name = 'Deepak'
sliced = name[0:3]      # This will give the string with characters from index 0 to 2 which means the upper bound is excluded (Slicing example)
print(sliced)

print(name[1])          # This will print the character present at 1st index in the string which is 'e'


# If we don't mention the lower bound, it means from the beginning or 0th index
print(name[:4])


# If we don't mention the upper bound, it means the entire length
print(name[1:])


# We can also add a skip value in slicing
word = 'amazing'
print(word[1::2])


# Methods of string...

print(name.len())
print(name.endswith('ak'))
print(name.startswith('d'))
print(name.lower())
print(name.upper())
# and mnany more...
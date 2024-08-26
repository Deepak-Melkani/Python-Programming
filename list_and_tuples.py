# Lists are mutable and enclosed within [ ]
# Lists elements can be accessed using indices 
# Slicing is possible similar to strings 
# Multiple data types are allowed in a single list

list = [1, 5.3, True, "Hello World"]

# List Methods

list.append(82)
list.sort()
list.reverse()
list.insert(3, 8)
list.pop(2)
list.remove(1)
# and many more



# Tuples are immutable and enclosed within ( )
# () denotes an empty tuple 
# a = (1) is not considered to be a tuple, to make it a tuple we need to mention a comma after writing 1
# Tuple elements can be accessed using indices 

tup = (1, 5, "Hello", False)


# Tuple Methods

len(tup)
cnt = tup.count(1)
tup.index(5)
# pip install name_of_module is a command used to install some module in the device
# This command is given on the terminal
# The installed module can be used in the program with the help of import keyword 

import pyjokes as pj

joke = pj.get_joke()
print("Printing joke...")
print(joke)


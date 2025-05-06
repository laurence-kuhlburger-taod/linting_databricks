# Unused imports
import os
import sys

# Function has unused arguments and bad indentation
def add_numbers( a, b ):
   result = a+b
   print( "Result is:", result )  # Extra spaces in parentheses
 return result   # Incorrect indentation for return

# Bad naming conventions and variables defined but never used
DEF_CONSTANT = 42  # Should use lowercase for constants in Python
myVariable = 10  # Bad naming style; should use snake_case
_unused_var = 100  # Prefix indicates unused, but better to remove it

# Extra whitespace, trailing commas, and missing newlines
def greet(name, ):
    print( "Hello,", name, )   # Extra comma, unnecessary spaces
    print(" This is an improperly formatted string.") 

# Block missing proper structure
if True:
    value = 1  
    file   = "test.txt"  # Excess spaces around the `=` operator
    print ("Empty block structure.") # Space after print keyword

# Final newline missing
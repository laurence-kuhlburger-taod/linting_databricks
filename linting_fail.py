def example_function(one, two):
  print("Hello world!")       # Unused variables and spacing issues

def unused_function(arg1, arg2):
    pass                      # This will trigger a "function is defined but never used" warning

x  =  1     # Extra spaces around the assignment operator

if x==1:    # Missing spaces around the comparison operator
    print ("This line has extra spacing in the parentheses.") # Spacing issues
print( "Another bad spacing here!") # Issue: space after `print(`

import os  # This is an unused import which will also trigger Ruff linting errors
import sys # Unused import


print("Ughhhh why isn't the bot    working :(")

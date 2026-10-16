"""
You can also use the print() function to display numbers:
However, unlike text, we don't put numbers inside quotes:
"""
print(3)
print(358)
print(50000)

# You can also do math inside the print() function:
print(3 + 3)
print(2 * 5)

#Mix Text and Numbers
#You can combine text and numbers in one output by separating them with a comma:
print("I am", 25, "years old.")

"""
Variable Names:
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. Variable names are case-sensitive (age, Age and AGE are three different variables)
5. A variable name cannot be any of the Python keywords.
"""
# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:
"""
2myvar = "John"
my-var = "John"
my var = "John"

"""

"""
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
"""
x, y, z = "KSA", "India", "USA"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
#And you can assign the same value to multiple variables in one line:
x = y = z = "Baltimore"
print(x)
print(y)
print(z)

"""
Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables.
This is called unpacking.
"""
print("Unpacking a Collection:")
fruits = ["KSA", "India", "USA"]
x, y, z = fruits
print(x)
print(y)
print(z)

"""
Output Variables
The print() function is often used to output variables.
"""
x = "Python is awesome"
print(x)

#In the print() function, you output multiple variables, separated by a comma:
x = "Python "
y = "is "
z = "awesome "
print(x, y, z)
#Out put will be : Python is awesome

#You can also use the + operator to output multiple variables (concatenate):
x = "Python"
y = "is"
z = "awesome"
print(x+ y + z)

#Out put will be : Pythonisawsome

x = "Python "
y = "is "
z = "awesome"
print(x+ y + z)

#Out put will be : Python is awesome

"""
Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()

# Output will be : Python is awesome


"""
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
The global variable with the same name will remain as it was, global and with the original value.
"""

# Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Output will be : Python is fantastic
# Output will be : Python is awesome    

x = "Great"
y= "person"

def myfunc():
  x = "Good"
  print("Ali is " + x + " " + y)

myfunc()

print("Ali is " + x + " " + y)

# Output will be : Ali is Good person
# Output will be : Ali is Great person  
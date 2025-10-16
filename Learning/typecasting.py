#Change the data type of a value to another data type
#You can convert from one data type to another with the following functions:
#int() - converts to integer
#float() - converts to float
#str() - converts to string
#list() - converts to list
#tuple() - converts to tuple
#set() - converts to set
#dict() - converts to dictionary
#Example
x = 5       # int
y = 3.14    # float
z = "Hello" # string
a = [1, 2, 3] # list
b = (4, 5, 6) # tuple
c = {7, 8, 9} # set
d = {"name": "Alice", "age": 30} # dictionary
#Convert int to float
x_float = float(x)
print(x_float) # Output: 5.0

#Convert float to int
y_int = int(y)
print(y_int) # Output: 3

#Convert int to string
x_str = str(x)
print(x_str) # Output: "5"

#Convert string to int (only if the string is a valid integer)
z_int = int("10")
print(z_int) # Output: 10

#Convert list to tuple
a_tuple = tuple(a)
print(a_tuple) # Output: (1, 2, 3)

#Convert tuple to list
b_list = list(b)
print(b_list) # Output: [4, 5, 6]

#Convert list to set
c_set = set(a)
print(c_set) # Output: {1, 2, 3}

#Convert set to list
c_list = list(c)
print(c_list) # Output: [7, 8, 9] (order may vary)

#Convert dictionary keys to list
d_keys = list(d.keys())
print(d_keys) # Output: ['name', 'age']

#Convert dictionary values to list
d_values = list(d.values())
print(d_values) # Output: ['Alice', 30]

#Convert dictionary items to list of tuples
d_items = list(d.items())
print(d_items) # Output: [('name', 'Alice'), ('age', 30)]

#Note: When converting from float to int, the decimal part is truncated (not rounded).
#What is truncated?
#Truncation means cutting off the decimal part of a number without rounding.
#Also, converting a string to an int or float will raise an error if the string is not a valid number.
#When converting a list to a set, duplicate values are removed since sets do not allow duplicates.
#When converting a set to a list, the order of elements may change since sets are unordered collections.
#Always ensure that the data you are converting is compatible with the target data type to avoid errors.
#For example, trying to convert a non-numeric string to an integer will raise a ValueError:

# invalid_str = "Hello"
# invalid_int = int(invalid_str)  # This will raise a ValueError


# More type casting examples
# Mainly type casting can be done with these data type functions:

# 1. int(): Python Int() function take float or string as an argument and returns int type object.
# 2. float(): Python float() function take int or string as an argument and return float type object.
# 3. str(): Python str() function takes float or int as an argument and returns string type object.

# int variable
a = 5

# typecast to float
n = float(a)

print(n)
print(type(n))

# int variable
a = 5.9

# typecast to int
n = int(a)

print(n)
print(type(n))

# int variable
a = 5

# typecast to str
n = str(a)

print(n)
print(type(n))

# string variable
a = "5.9"

# typecast to float
n = float(a)

print(n)
print(type(n))
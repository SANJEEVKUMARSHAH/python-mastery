
# ============================================================
# PYTHON BASICS
# Topic: Output, Input, Variables, Data Types, Operators,
#        Type Conversion, and Basic Mathematical Problems
# ============================================================


# ------------------------------------------------------------
# 1. OUTPUT STATEMENT
# ------------------------------------------------------------
# The print() function is used to display information on the
# screen. It can display strings, variables, numbers, and more.

print("Hello, Python!")
print("My name is Sanjeev")

# Creating a variable and printing its value
name = "Ram"

print("Name is", name)
print(name)

# Printing multiple values
age = 20
print("Name:", name, "Age:", age)

# Printing different data types
print(10)
print(3.14)
print(True)


# ------------------------------------------------------------
# 2. INPUT STATEMENT
# ------------------------------------------------------------
# The input() function allows the user to enter information.
# By default, input() always returns a string.

username = input("Enter your username: ")

print("Your username is:", username)

# Taking multiple inputs
full_name = input("Enter your full name: ")
city = input("Enter your city: ")

print("My name is", full_name, "and I live in", city)


# ------------------------------------------------------------
# 3. COMMENTS IN PYTHON
# ------------------------------------------------------------
# Comments are used to explain code.
# Python ignores comments during program execution.

# This is a single-line comment.

# This is another comment.
# Each line starts with the # symbol.

# Python does not have a separate multiline comment syntax.
# We can write multiple single-line comments using #.

# Example:
# This program takes two numbers
# and displays their sum.

# Triple-quoted strings are NOT technically comments.
# They are commonly used for documentation (docstrings).

"""
This is a multiline string.
It is not a comment.
It can be used as a module or function docstring.
"""


# ------------------------------------------------------------
# 4. VARIABLES AND IDENTIFIERS
# ------------------------------------------------------------
# A variable is a name used to store a value.
# An identifier is the name given to a variable, function, etc.

student_name = "Sanjeev"
student_age = 20
student_gpa = 3.62

print(student_name)
print(student_age)
print(student_gpa)

# Rules for naming variables:
# 1. Variable names are case-sensitive.
# 2. They can contain letters, digits, and underscores.
# 3. They cannot start with a digit.
# 4. They cannot contain spaces.
# 5. They cannot be Python keywords.
# 6. Use meaningful names for better readability.

# Case-sensitive examples:
name = "Ram"
Name = "Shyam"

print(name)  # Ram
print(Name)  # Shyam

# Valid variable names:
student_name = "Ram"
age2 = 20
_total = 100

# Invalid variable names:
# 2age = 20          # Cannot start with a digit
# student name = ""   # Cannot contain spaces
# class = "Python"    # Cannot use a keyword


# ------------------------------------------------------------
# 5. DATA TYPES IN PYTHON
# ------------------------------------------------------------
# A data type defines the kind of value stored in a variable.

# Integer (int): Whole numbers, positive, negative, or zero
a = 10
b = -5
c = 0

# Float (float): Numbers containing decimal points
price = 99.99
temperature = -2.5

# String (str): Text enclosed in quotes
first_name = "Sanjeev"
message = 'Welcome to Python'

# Boolean (bool): Represents True or False
is_student = True
is_graduated = False

# Checking data types using type()
print(type(a))            # <class 'int'>
print(type(price))        # <class 'float'>
print(type(first_name))   # <class 'str'>
print(type(is_student))   # <class 'bool'>

# Python is dynamically typed.
# We do not need to declare a variable's type explicitly.

value = 10
print(value, type(value))

value = "Python"
print(value, type(value))


# ------------------------------------------------------------
# 6. PYTHON KEYWORDS
# ------------------------------------------------------------
# Keywords are reserved words with special meanings in Python.
# They cannot be used as variable names.

# Examples:
# False, None, True, and, or, not, if, else, for, while,
# async, await, class, def, return, import, etc.

# Incorrect:
# class = "Computer Engineering"

# Correct:
class_name = "Computer Engineering"

# Note: Python keywords are case-sensitive.
# False, None, and True are capitalized exactly this way.


# ------------------------------------------------------------
# 7. PYTHON NAMING CONVENTIONS
# ------------------------------------------------------------
# Naming conventions help make code readable and consistent.

# Snake case: Commonly used for variables and functions
student_name = "Ram"
total_price = 500

# Camel case: First word lowercase, later words capitalized
studentName = "Ram"
totalPrice = 500

# Pascal case: Every word starts with a capital letter
StudentName = "Ram"
TotalPrice = 500

# Recommended Python style:
# Use snake_case for variables and functions.
# Use PascalCase for class names.
# Use UPPER_CASE for constants.

PI = 3.14159
MAX_STUDENTS = 100


# ------------------------------------------------------------
# 8. ARITHMETIC OPERATORS
# ------------------------------------------------------------
# Arithmetic operators perform mathematical calculations.

a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a // b)  # Floor division: 3
print(a % b)   # Modulus (remainder): 1
print(a ** b)  # Exponentiation: 1000

# Example of exponentiation:
print(2 ** 3)  # 2 raised to the power of 3 = 8

# Example of modulus:
print(10 % 3)  # Remainder = 1


# ------------------------------------------------------------
# 9. RELATIONAL / COMPARISON OPERATORS
# ------------------------------------------------------------
# Comparison operators compare two values.
# They return either True or False.

a = 10
b = 20

print(a == b)  # Equal to: False
print(a != b)  # Not equal to: True
print(a > b)   # Greater than: False
print(a < b)   # Less than: True
print(a >= b)  # Greater than or equal to: False
print(a <= b)  # Less than or equal to: True


# ------------------------------------------------------------
# 10. ASSIGNMENT OPERATORS
# ------------------------------------------------------------
# Assignment operators assign or update variable values.

a = 5

a += 2   # Same as a = a + 2
print(a)  # 7

a -= 3   # Same as a = a - 3
print(a)  # 4

a *= 2   # Same as a = a * 2
print(a)  # 8

a /= 4   # Same as a = a / 4
print(a)  # 2.0

a //= 2  # Same as a = a // 2
print(a)  # 1.0

a %= 2   # Same as a = a % 2
print(a)  # 1.0


# ------------------------------------------------------------
# 11. LOGICAL OPERATORS
# ------------------------------------------------------------
# Logical operators combine or reverse Boolean conditions.

# AND: True only when both conditions are True
print(5 > 3 and 10 > 5)  # True
print(5 > 3 and 10 < 5)   # False

# OR: True when at least one condition is True
print(5 > 3 or 10 < 5)   # True
print(5 < 3 or 10 < 5)   # False

# NOT: Reverses the Boolean result
print(not (3 > 5))  # True
print(not (5 > 3))  # False


# ------------------------------------------------------------
# 12. OPERATOR PRECEDENCE
# ------------------------------------------------------------
# Operator precedence determines which operation is performed
# first when an expression contains multiple operators.

# General order (higher to lower):
#
# 1. ()                  Parentheses
# 2. **                  Exponentiation
# 3. +x, -x, ~x          Unary operators
# 4. *, /, //, %         Multiplication and division
# 5. +, -                 Addition and subtraction
# 6. <, <=, >, >=, ==, != Comparisons
# 7. not                  Logical NOT
# 8. and                  Logical AND
# 9. or                   Logical OR
#
# Operators at the same precedence level are generally
# evaluated from left to right.
#
# Exponentiation is an important exception:
# It is evaluated from right to left.

print(2 + 3 * 4)     # 14
print((2 + 3) * 4)   # 20

print(10 / 2 * 5)    # 25.0
# Division and multiplication have equal precedence.
# Evaluation happens from left to right:
# (10 / 2) * 5 = 25

print(2 ** 3 ** 2)   # 512
# Exponentiation is evaluated from right to left:
# 2 ** (3 ** 2) = 2 ** 9 = 512


# ------------------------------------------------------------
# 13. TYPE CONVERSION
# ------------------------------------------------------------
# Type conversion means changing a value from one data type
# to another.

# Common conversion functions:
# int()    -> Converts to an integer
# float()  -> Converts to a floating-point number
# str()    -> Converts to a string
# bool()   -> Converts to a Boolean value

# Explicit type conversion (also called type casting)
number = int(10.8)
print(number)        # 10

decimal = float(5)
print(decimal)       # 5.0

text = str(100)
print(text, type(text))  # 100 <class 'str'>

# Implicit type conversion:
# Python automatically converts compatible numeric types.

result = 5 + 10.0

print(result)        # 15.0
print(type(result))  # <class 'float'>

# Important:
# int() removes the decimal part; it does not round.
print(int(5.9))      # 5
print(int(-5.9))     # -5

# Converting a numeric string:
number = int("25")
print(number + 5)    # 30

# Invalid conversion:
# int("hello")       # ValueError


# ------------------------------------------------------------
# 14. PROBLEM: SUM OF TWO NUMBERS
# ------------------------------------------------------------
# Problem:
# Take two numbers from the user and display their sum.

# Incorrect approach:
# input() returns a string by default.
# Therefore, + joins the strings instead of adding numbers.

a = input("Enter the first number: ")   # Example: 5
b = input("Enter the second number: ")  # Example: 6

sum_result = a + b

print(sum_result)  # Output: 56

# Correct approach:
# Convert the input values into numbers before adding them.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

sum_result = a + b

print("The sum is:", sum_result)

# Example:
# Input: 5 and 6
# Output: The sum is: 11.0


# ------------------------------------------------------------
# 15. PROBLEM: AVERAGE OF TWO NUMBERS
# ------------------------------------------------------------
# Problem:
# Take two numbers from the user and calculate their average.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

average = (a + b) / 2

print("The average is:", average)

# Example:
# Input: 5 and 6
# Output: The average is: 5.5


# ------------------------------------------------------------
# 16. ADDITIONAL PRACTICE: AREA OF A RECTANGLE
# ------------------------------------------------------------
# Formula:
# Area = Length * Breadth

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

area = length * breadth

print("The area of the rectangle is:", area)


# ------------------------------------------------------------
# 17. ADDITIONAL PRACTICE: SIMPLE INTEREST
# ------------------------------------------------------------
# Formula:
# Simple Interest = (Principal * Rate * Time) / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100

print("The simple interest is:", simple_interest)


# ============================================================
# END OF PYTHON BASICS
# ============================================================

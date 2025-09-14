# File: homework1. py
# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals
b = 1.5
print(b)
print(type(b)) # b is a float, a decimal number
c = 3j
print(c)
print(type(c)) # c is a complex, a complex number
d = "hello"
print(d)
print(type(d)) # d is a str, a sequence of characters
e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, an ordered set of stuff and can be changed
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, which is a datatype of things that are connected
g = (1, 2)
print(g)
print(type(g)) # g is a tuple, an ordered collection of things but it cannot be changed
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, an ordered set of stuff and can be changed
i = True
print(i)
print(type(i)) # i is a bool, which is true or false
j = None
print(j)
print(type(j)) # j doesn't have a type or is "NoneType", it's nothing
k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, an ordered set of stuff and can be changed
l = str(14)
print(l)
print(type(l)) # l is a str, a sequence of characters
m = 1e4
print(m)
print(type(m)) # m is a float, a decimal number
# 1. How many different data types did you find?
#   8 different type: str, float, list, nonetype, tuple, dict, complex, int
#   or 7 if you don't count none
# 2. List all the data types you found.
#   str, float, list, nonetype, tuple, dict, complex, int
# 3. What variables have the same data types?
#   m&b,h&k,l&d
# 4. What was the data type of l? Why is it not an integer? What does str() do?
#   l was a string, it wasn't an int because str() was used on it, str() turns whatever is in the parenthesis into a string
# 5. Look up one more data type not given above. Repeat the same procedure.
#   a set in python is a collection of unordered items that can be changed but it has no order

# --- Booleans ---
print(10 > 9)	# True, 10 is greater than 9
print(10 == 9)	# False, 10 is not equal to 9
print(10 <= 9)	# False, 10 is not less than or equal to 9
print(bool("abc"))	# True, non-empty string is True
print(bool(123))	# True, non-zero number is True
print(bool(["apple", "cherry", "banana"]))	# True, lists with things inside are True
print(bool(True))	# True, True is True
print(bool(False))	# False, False is False
print(bool(0))	# False, 0 is considered False
print(bool(""))	# False, empty string is False
print(bool(" "))	# True, string with a space is non-empty so True
print(bool(()))	# False, empty tuple is False
print(bool([]))	# False, empty list is False
print(bool({}))	# False, empty dictionary is False
print(bool(True and False))	# False, True and False is False
print(bool(True and True))	# True, True and True is True
print(bool(False and False))	# False, False and False is False
print(bool(True or False))	# True, True or False is True
print(bool(True or True))	# True, True or True is True
print(bool(False or False))	# False, False or False is False
print(bool(not(False)))	# True, not False is True
print(bool(not(True)))	# False, not True is False
# What pattern do you notice about expressions returning True or False?
#   it only returns true when the inside of the print is true and vice versa with false
# Which expression surprised you about its result?
#   bool(" ") surprised me because I thought an empty string would be false but a string with a space is true
# Create an expression, not given above, that will return True. Why is it True?
#   print(bool({1, 2, 3})) True, because a non-empty set is considered True in Python
# Create an expression, not given above, that will return False. Why is it False?
#   print(bool({})) False, because it's an empty set

# --- Operators ---
print(10 + 5)	# 15, + performs addition
print(10 - 5)	# 5, - does subtraction
print(2 * 4)	# 8, * does multiplication
print(6 / 3)	# 2.0, / does division and returns a float(even tho 6/3 is an int)
print(5 % 2)	# 1, % returns the remainder, called modulus
print(3 ** 2)	# 9, ** raises to the power of
print(15 // 2)	# 7, // performs floor division(floor of 15/2 which is 7)
print(5 == 2)	# False, == checks if values are equal
print(10 != 10)	# False, != checks if values aren't equal
print(2 < 5)	# True, < checks if left less than right
print(12 > 5)	# True, > checks if left greater than right
print(5 <= 6)	# True, <= checks if left less than or equal than right
print(1 >= 10)	# False, >= checks if left greater than or equal right
x = 5
x += 5	# x = 10, adds 5 to x, 
x -= 4	# x = 6, subtracts 4 from x
x *= 3	# x = 18, multiplies x by 3
print(x)	# 18, prints the final value of x which is 18
# Answer the following questions as comments:
# 1. What does the operator and do? Write an expression that results in True. Write an expression
# that results in False.
#   the and operator returns true if both values are true, otherwise it's false, 
# print(2 > 5 and 3 > 1)
# 2. What does the operator or do? Write an expression that results in True. Write an expression
# that results in False.
#   the or operator returns false if both of them are false, otherwise it's true
# print(2 > 5 or 3 < 1)
# 3. What does the operator not do? Write an expression that results in True. Write an expression
# that results in False.
#   the not operator just reverses whatever it's done to, ex: not true = false and not false = true
# print(not(3<5))
# What is the difference between / and //?
#   / returns the decimal number of the division whereas // rounds that value down
# 2. What is the difference between % and //?
#   % gives the remainder such as 5%2=1 but 5//2 = 2 because 5/2=floor(2.5)=2
# 3. What operator would you use to calculate the remainder when dividing two numbers? Give
# an example.
#   % operator because it returns the remainder, if we wanted to find remainder of 10/3 we use 10%3=1
# 4. How do assignment operators work?
#   assignment operators change the value of a variable by doing the operation and then assigning the result of that operator
#   ex: x=5, x=x+3 would result in x=8 cuz 5+3=8
# --- Strings ---

my_string = "hello"
print(my_string) # Prints: hello
print(my_string)            # Prints: hello
print(my_string[0])         # Prints: h
print(my_string[1])         # Prints: e
print(my_string[2])         # Prints: l
print(my_string[3])         # Prints: l
print(my_string[4])         # Prints: o
print(my_string[-1])        # Prints: o (last character)
print(my_string[1:3])       # Prints: el (characters at index 1 and 2)
print(my_string[0:5:2])     # Prints: hlo (characters at index 0, 2, 4)
print(len(my_string))       # Prints: 5 (the length of the string "hello")
print(my_string + "goodbye")# Prints: hellogoodbye (concatenates the two strings)
print(my_string*7)          # Prints: hellohellohellohellohellohellohello (repeats the string 7 times)
# 1. Define the term slicing. For which of the manipulations did you slice your string?
#   it just means to get a section of the string, 8 and 9 used slicing
# 2. Call the following, describe the result:
# name = "Oski"
# print("Hello, my name is", name)
#   the result is "Hello, my name is Oski" 
# 3. Call the following, describe the result.
# name = "Oski"
# print(f"Hello, my name is {name}")
#   the result is "Hello, my name is Oski" 
# 4. What is the difference between the two last print statements?
# Hint: Look up f-strings.
#   the difference is we used a comma to add oski to the first print but in the second one we were able to throw in oski directly into the quotes

# --- Terminal Commands ---
# cd, change directory, Use it to move from one folder to another, ex cd desktop
# ls, list directory contents, use it to see what's inside the folder you're in, ex ls to see what's in the folder
# ls -a, List contents including hidden files (Files that start with a dot), ex ls-a to see all the files and hidden ones
# mkdir, Make directory, use it to open a directory where you're at, ex mkdir hw2
# cat, concatenate, use it to view the file, ex cat datatypes.py
# pwd, gives the path to the directory you're in rn, use it to see all the children folders you went through, ex pwd
# cd .. Change to parent directory, use to go out one director, ex cd ..
# cd . keeps you in the same directory, use to stay where you are?, ex cd .
# cd ∼ Change to home directory, use to go home, ex cd ∼
# cp copy file, use to copy files, ex cp datatypes.py
# mv move file, use to move files, ex mv [datatypes.py] [hw1]
# rm (be careful with this one) remove file, use to remove files, ex rm datatypes.py
# clear, empties all the stuff that was there before
# grep, search for a term in a file i think it's like ctrl f?, use to find words, grep [int] [datatypes.py]
# 1. look up 3 other commands not present. Define and explain how to use them on the command line
    # touch: Creates a new empty file. Usage: touch filename.txt
    # head: Shows the first 10 lines of a file. Usage: head filename.txt
    # tail: Shows the last 10 lines of a file. Usage: tail filename.txt
# 2. What is the difference between ls and ls -a?
#   ls only shows the nonhidden files, ls -a shows hidden ones and the regular ones
# 3. What is a hidden file?
#   file starting with a .
# 4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to use them on the command line.
#   -l: Used with ls, shows detailed (long) listing of files. Usage: ls -l
#   -r: Used with ls, List contents reverse order. Usage: ls -r
#   -h: Used with ls -l, shows file sizes in human-readable format (KB, MB). Usage: ls -lh
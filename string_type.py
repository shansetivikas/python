# Strings are sequence of characters, using the syntax of either single quotes or double quotes
# len is used to get length of string

# Indexing
# These actions use [] square brackets and index to get character

# String      -      H  e  l  l  o 
# Index       -      0  1  2  3  4
# reverse index -    0 -4 -3 -2  -1

# Slicing
# -> [start:stop:step]
# -> start is a numerical index for the slice start
# -> stop is the index you will go up to (but not include)
# -> step is the size of the jump you take

print('hello')

print("hello")

print("I don't do that")

print("hello \nworld")

print("hello \tworld")

print(len("hello"))

mystring = "hello world"

print(mystring[0])

print(mystring[1])

print(mystring[0:3:1])

print(mystring[0:3])

print(mystring[-3])

print(mystring[2:])

#reverse string
print(mystring[::-1])

name = "Vikas"
# name[0] = "p" shows issues we cant change string its immutable

data = "Hello world"

print(data.split())
print(data.upper())
print(data.lower())
# print(data.split(e))
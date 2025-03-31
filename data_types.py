# sring daya type

# Literal assignment
import math
first = "dave"
last = "gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multipline lines
multiline = '''
Hey, how r u?

I was just checking in.
                                all gud?

'''
print(multiline)

# Escaping Special characters
sentence = 'I\'m back at work!\they!\n\nwhere\'s this at\\located?'
print(sentence)

# String methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("gud", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                          "
multiline = "                        " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))


# Build a Menu
title = "menu".upper()
print(title.center(20, "="))
print(" Coffee".ljust(16, ".") + "$1".rjust(4))
print(" tea".ljust(16, ".") + "$3".rjust(4))
print(" milk".ljust(16, ".") + "$5".rjust(4))

print("")

# String Index Values
print(first[0])
print(first[-1])
print(first[1:])


# Some method return boolean data
print(first.startswith("d"))
print(first.endswith("z"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))


# Numeric Data Types

# Integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# built i function for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))


print(math.pi)

# Casting a string to a number
zipcode = "100001"
zip_value = int(zipcode)
print(type(zip_value))

3 Error if you attempt to cast a incorrect data
zip_value = int("New York")

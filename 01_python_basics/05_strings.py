# ++++++++++ Multiline Strings ++++++++++
"""
NOTE: Strings in python are surrounded by either single quotation marks,
or double quotation marks: 'hello' is the same as "hello".
"""

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

# You can display a string literal with the print() function:
print("Hello")
print('Hello')
print(a)


# Like many other popular programming languages, strings in Python
# are arrays of bytes representing unicode characters.
# However, Python does not have a character data type,
# a single character is simply a string with a length of 1.



# ++++++++++ Square brackets can be used ++++++++++
# ++++++++++ to access elements of the string. ++++
print('Get the character at position 1:')
a = "Hello, World!"
print('a', a)
print('a[1]', a[1])




# ++++++++++ Looping Through a String ++++++++++

# Since strings are arrays, we can loop through
# the characters in a string, with a for loop.
print('Loop through the letters in the word "banana"')
for x in "banana":
  print(x)



# ++++++++++ String Length ++++++++++

# To get the length of a string, use the len() function.
print('The len() function returns the length of a string:')
a = "Hello, World!"
print('a', a)
print('len(a)', len(a))


# ++++++++++ To check if a certain phrase or character is present ++
# ++++++++++ in a string, we can use the keyword in. +++++++++++++++

# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print('txt', txt)
print('"free" in txt ->', "free" in txt)



# ++++++++++ Use it in an if statement ++++++++++

# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


# ++++++++++ To check if a certain phrase or character ++++
# ++++++++++ is NOT present in a string, we can use +++++++
# ++++++++++ the keyword not in. ++++++++++++++++++++++++++

# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print('txt', txt)
print('"expensive" not in txt', "expensive" not in txt)

# Use it in an if statement:
# print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")




# ++++++++++++++++++++++++++ Slicing ++++++++++++++++++++++++++

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon,
# to return a part of the string.
string = 'Hello, world!'
print(f'string: {string}')
print(f'Printing position of {string} (string[2:5]): {string[2:5]}')  # output: llo

# By leaving out the start index, the range will start at the first character
print(f'Printing position of {string} (string[:5]): {string[:5]}') # output: Hello 

# By leaving out the end index, the range will go to the end
print(f'Printing position of {string} (string[2:]): {string[2:]}') # output: llo, world!

# Use negativa indexes to start the slice from the end of the string
# from 'o' in 'world!' (position -5) to, but not included 'd' in 'world' (position -2)
print(f'Printing position of {string} (string[-5:-2]): {string[-5:-2]}')  # output: orl



# ++++++++++++++++++++++++ Modify Strings ++++++++++++++++++++++++

# Python has a set of built-in methods that you can use on strings.
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(f'a = {a}')
print('a.upper()', a.upper()) # returns "HELLO, WOLRD!"

# The lower() method returns the string in lower case:
a = "Hello, World!"
print('a.lower()', a.lower()) # returns "hello, world!"

# Whitespace is the space before and/or after the actual text,
# and very often you want to remove this space.
a = " Hello, World! "
print('a.strip()', a.strip()) # returns "Hello, World!"

# The replace() method replaces a string with another string:
a = "Hello, World!"
print('a.replace("H", "J")', a.replace("H", "J"))

# The split() method returns a list where the text between the specified separator becomes the list items.
# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print('a.split(",")', a.split(",")) # returns ['Hello', ' World!']
print('a.split("o")', a.split("o")) # returns ['Hello', ' World!']



# ++++++++++++++++++++++ String Concatenation ++++++++++++++++++++++

# To concatenate, or combine, two strings you can use the + operator.
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print('c', c)

# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print('c', c)

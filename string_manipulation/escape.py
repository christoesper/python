# a program to demonstrate escaping

# the below DOES NOT work:

# name = 'Christopher's'
# print(name)

# this DOES work:

single_quote = 'Christopher\'s'
print(single_quote)

# for double quotes

double_quote = "He said, \"Hi!\"" # will output He said, "Hi!"

# for backslashes

backslash = "C:\\Users\\John"
print(backslash) # will output C:\Users\John

# new lines, start a new line (enter key)

new_line = "Hello\nWorld"   # you need the backslash AND the n
print (new_line) # outputs Hello
#                         World

# tabs, adds extra (white)spaces

tab = "A\tB\tC"  # this time you need the backslash AND the t
print(tab)

# backspace (deleteing a character)

backspace = "Hello\b!" # you need the backslash AND the b
print(backspace)

# carraige return, anything after \r replaces the same amount of characters at the starts

#takes the cursor to the beginning of the line and replaces the character


carraige_r = "123\rABC" # you need the backslash AND the r
print(carraige_r) # outputs 'ABC'

# unicode character, allows a special character to be entered - is in the form of \uXXXX

uni = "\u03A9" # IS, AGAIN, \uXXXX
print(uni) # outputs the greek omega character, Ω






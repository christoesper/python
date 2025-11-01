# Slicing: Extracting parts of a string

# Slicing
# 0 1 2
# A P P

word = "PYTHON"

# 0 1 2 3 4 5
# P Y T H O N

print(word[3], word[4], word[5])

sentence = "I am a boy, I live on Earth"
print(sentence[19],sentence[20])
print(sentence[0],sentence[1],sentence[2],sentence[3],sentence[4],sentence[5],sentence[6],sentence[7],sentence[8],sentence[9])

# sentence is the variable name, dataType is string, value is "I am a boy, I live on Earth"
# [] accepts two arguments, first is the "Start point" while the second argument is the "End point".
# They are separated by a colun ":"
# These argument are strictly indexes, and integers.

print(sentence[0:10])     # prints I am a boy

print(sentence[12:27])    # prints out I live on Earth

print(sentence[-1:])      # gets the last character

print(word[-4:-1])        # prints THO
print(word[2:5])          # also prints THO

name = "John Doe"
initials = name[0],name[5]
reverse_initials = name[-8],name[-3]
print(initials)    # prints first characters of first and last name
print(reverse_initials)  # prints first characters of first and last name
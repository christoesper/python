# Indexing: Accessing characters in a string using their position

# spaces count as characters

word = "PYTHON"

# to print 'T'
print(word[2])

#to print 'TH'
print(word[3], word[4])



# Indexing strings
# 0 1 2 3 4
# A P P L E


# Slicing
# 0 1 2
# A P P

word = "PYTHON"

# 0 1 2 3 4 5
# P Y T H O N

print(word[3], word[4], word[5])

sentence = "I am a boy, I live on Earth"
print(sentence[19],sentence[20])
print(sentence[0],sentence[1],sentence [2],sentence [3],sentence [4],sentence [5],sentence[6],sentence[7],sentence [8],sentence[9])

# sentence is the variable name, dataType is string, value is "I am a boy, I live on Earth"
# [] accepts two arguments, first is the "Start point" while the second argument is the "End point".
# They are separated by a colun ":"
# These argument are strictly indexes, and integers.
print(sentence[0:10])
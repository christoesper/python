# name = input("what is your full name?: ")
name = "christopher chukwu"  
strip = name.strip()
print("this is a strip ; ", strip)
upper = name.upper()
print("\"Hello,", upper,"!" "\nWelcome to Python learning!")



# strip method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
name = "Christopher   "
stripped_name = name.strip()
replaced_name = stripped_name.replace("+", "")   # replace method replaces a string with another string
capitalised_name = stripped_name.upper()  # upper method converts all lowercase characters in a string into uppercase characters 
lower_cap_name = capitalised_name.lower() # lower methond converts all uppercase characters in a string into lowercase characters
reversed_name = lower_cap_name[::-1]
count_of_substring = reversed_name.count('a') # count method counts the number of occurences of a substring in a string
find_index_of_substring = reversed_name.find("t")   # find method finds the first occurence of a substring in a string and returns its index


print('Stripped name :-', stripped_name)
print('Replaced name :-', replaced_name)
print('Capitalised name :-', capitalised_name)
print('lowercased name :-', lower_cap_name)
print('Reversed name :-', reversed_name)
print("Count of 'a' in lowercased name :-", count_of_substring)
print("Index of 't' in reversed_name :-", find_index_of_substring)
# Intermediate Python Exercises
# Exercise 1: List Comprehension Mastery
# Practice Problem: Write a single-line list comprehension that takes a list 
# of strings, filters out strings shorter than 4 characters, and converts the 
# remaining strings to uppercase.

# Exercise Purpose: List comprehensions are a hallmark of Pythonic code. They 
# allow you to replace verbose for loops and .append() calls with a readable, 
# optimized single line. This exercise teaches you how to combine 
# transformation (uppercase) and filtering (length check) in one expression.

# words = ["apple", "bat", "cherry", "dog", "elderberry"]
# filtered_words = [word.upper() for word in words if len(word) > 4]
# print(filtered_words)



# ==========================================================================



# Exercise 2: Dictionary Merging with Logic
# Practice Problem: Write a function that merges two dictionaries. If a key 
# exists in both dictionaries, sum their values. If a key exists in only one, 
# include it as is.

# Exercise Purpose: Real-world data often comes from multiple sources. Simply 
# using dict.update() would overwrite duplicate keys. This exercise introduces
# you to efficient dictionary iteration and the dict.get(key, default) method, 
# which is essential for avoiding KeyError.

# def merge_dicts(d1, d2):
# 	# start with a copy of d1 to avoid modifying the original
# 	result = d1.copy()

# 	for key, value in d2.items():
# 		result[key] = result.get(key, 0) + value

# 	return result 

# d1 = {'a': 10, 'b': 20} 
# d2 = {'b': 5, 'c': 15}

# merged = merge_dicts(d1, d2)
# print(f'Merged dictionary: {merged}')



# ==========================================================================



# Exercise 3: Frequency Map with Counter
# Practice Problem: Create a function that takes a string and returns a count 
# of how many times each character appears. Ignore spaces and make it 
# case-insensitive.

# Exercise Purpose: While you could build a frequency map with a standard loop, 
# Python’s collections module offers a specialized tool called Counter. This 
# exercise teaches you to leverage the Standard Library to write less code 
# while increasing performance.

# from collections import Counter
# def char_frequency(text):
# 	letters = text.lower().replace(" ", "")

# 	return Counter(letters)

# text = "Python Programming"
# print(f"Character Frequency: {char_frequency(text)}")
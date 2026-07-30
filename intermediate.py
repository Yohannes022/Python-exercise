# Intermediate Python Exercises
# Exercise 1: List Comprehension Mastery

# words = ["apple", "bat", "cherry", "dog", "elderberry"]
# filtered_words = [word.upper() for word in words if len(word) > 4]
# print(filtered_words)



# ==========================================================================



# Exercise 2: Dictionary Merging with Logic
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
# from collections import Counter
# def char_frequency(text):
# 	letters = text.lower().replace(" ", "")

# 	return Counter(letters)

# text = "Python Programming"
# print(f"Character Frequency: {char_frequency(text)}")
# Exercise 1. Arithmetic Product and Conditional Logic
# def multiplication_or_sum(num1, num2):
# 	if not isinstance(num1, int) or not isinstance(num2, int):
# 		return "Argument must be an integer value."
# 	result = num1 * num2
# 	if result <= 1000:
# 		return "The result is " + str(result)
# 	else:
# 		result = num1 + num2
# 		return "The result is " + str(result)
	
# print(multiplication_or_sum(100, 900))



# ========================================================================



# Exercise 2. Cumulative Sum of a Range
# print("Printing current and previous number sum in range(10)")
# previous_num = 0

# for num in range(10):
# 	x_sum = previous_num + num
# 	print(f"Current Number {num} Previous Number {previous_num} Sum: {x_sum}")

# 	previous_num = num



# ========================================================================



# Exercise 3. String Indexing and Even Slicing
# def even_index_num(word):
# 	if not isinstance(word, str):
# 		return "Argument must be a string."
# 	print(f"Original String is {word}")
# 	print("Printing only even index chars")
# 	for s in range(0, len(word) - 1, 2):
# 		print(word[s])

# even_index_num("Yohannes")

# # -------------------- OR --------------------

# print("Printing only even index chars")
# word = "John"
# print(f"Original String is {word}")
# even_char = word[::2]
# for char in even_char:
# 	print(char)




# ========================================================================



# Exercise 4. String Slicing and Substring Removal
# def remove_chars(word, num):
# 	return word[num:]

# print("Removing characters from a string")
# print(remove_chars("pynative", 4))
# print(remove_chars("pynative", 2))




# ========================================================================



# Exercise 5. Variable Swapping (The In-Place Method)
# def variable_swapping(a, b):
# 	print(f'Before Swap: a = {a}, b = {b}')
# 	a, b = b, a
# 	print(f'After Swap: a = {a}, b = {b}')

# print(variable_swapping("Johannes", "Yohannes"))



# ========================================================================



# Exercise 6. Calculating Factorial with a Loop
# def factorial(num):
# 	if not isinstance(num, int):
# 		return "Argument must be an integer value."
# 	prev = 1
# 	for i in range(1, num + 1):
# 		prev = prev * i

# 	return print(f'The factorial of {num} is {prev}')

# factorial(6)



# ========================================================================



# Exercise 7. List Manipulation: Add and Remove
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# def add_remove(word, num): 
# 	# word: for the fruit going to be added, 
# 	# num: the index where the fruit removed from the fruits list
# 	if not isinstance(word, str):
# 		return "The fruit must be a string."
# 	if not isinstance(num, int):
# 		return "The index / number the fruit removed from the list must be an integer"
	
# 	fruits.append(word)
# 	fruits.pop(num)

# 	return print(f"The updated fruit list: {fruits}")

# add_remove("fig", 1)



# ========================================================================



# Exercise 8. String Reversal
# def string_reversal(text):
# 	if not isinstance(text, str):
# 		return "Argument must be a string."
# 	return (f"Original: {text}\nReversed: {text[::-1]}")

# print(string_reversal("sennahoY"))



# ========================================================================



# Exercise 9. Vowel Frequency Counter
# def vowel_counter(text):
# 	vowels = "aeiou"
# 	count = 0

# 	if not isinstance(text, str):
# 		return "Argument must be a string."
	
# 	for char in text.lower():
# 		if char in vowels:
# 			count += 1

# 	return (f"Number of vowels in '{text}' is {count}")

# print(vowel_counter("Yohannes start learning from scratch doing exercise."))



# ========================================================================



# Exercise 10. Finding Extremes (Min/Max) in a List
# def extremes(nums):
# 	if not isinstance(nums, list):
# 		return "Argument must be a list."
	
# 	print(f"Largest: {max(nums)}\nSmallest: {min(nums)}")

# nums = [45, 2, 89, 12, 7]
# extremes(nums)



# ========================================================================



# Exercise 11. Removing Duplicates from a List
# def remove_duplicates(data):
# 	if not isinstance(data, list):
# 		return "Argument must be a list."
# 	return f"unique List: {list(set(data))}"

# print(remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5]))



# ========================================================================



# Exercise 12. List Comparison and Boolean Logic
# def start_end(nums):
# # Write a function to return True if the first and 
# # last number of a given list  is the same. 
# # If the numbers are different, return False.
# 	if not isinstance(nums, list):
# 		return "Argument must be a list."
# 	if nums[0] == nums[-1]:
# 		return print(f"Given liest: {nums} | result is True")
# 	else: return print(f"Given liest: {nums} | result is False")

# list1 = [10, 20, 30, 40, 10]
# list2 = [75, 65, 35, 75, 30]

# start_end(list1)
# start_end(list2)



# ========================================================================



# Exercise 13. Filtering Lists with Conditional Logic
# num_list = [10, 20, 33, 46, 55]
# print(f"Given list is: {num_list}")
# print(f"Divisible by 5: ")
# for num in num_list:
# 	if num % 5 == 0:
# 		print(num)



# ========================================================================



# Exercise 14. Substring Frequency Analysis
# def substring_freq(text, word):
# 	if not isinstance(text, str):
# 		return "Argument must be a string."
# 	if not isinstance(word, str):
# 		return "Argument must be a string."
	
	
# 	apperance = text.count(word)
	
# 	return print(f"{word} appered {apperance} times.")

# substring_freq("Emma is good developer. Emma is a writer", "Emma")



# ========================================================================



# Exercise 15. Nested Loops for Pattern Generation
# rows = int(input("Enter the number of rows to make a pyramid pattern: ")) 

# for i in range(rows):
# 	for j in range(i):
# 		print(i, end=" ")
# 	print("")

# # pyramid pattern of numbers
# print("\npyramid pattern of numbers")
# for i in range(1, rows + 1):
# 	for j in range(1, i+1):
# 		print(j, end=" ")
# 	print("")

# # Inverted pyramid pattern of numbers
# print("\nInverted pyramid pattern of numbers")
# b=0
# for i in range(rows, 0, -1):
# 	b+=1
# 	for j in range(1, i+1):
# 		print(b, end=" ")
# 	print("\r")

# # Inverted Pyramid pattern with the same digit
# print("\nInverted Pyramid pattern with the same digit")
# num = rows
# for i in range(rows, 0, -1):
# 	for j in range(0, i):
# 		print(num, end=" ")
# 	print("\r")



# ========================================================================



# Exercise 16. Numerical Palindrome Check
# def palindrome_check(num):
# 	if not isinstance(num, int):
# 		return "Argument must be an integer."
# 	str_num = str(num)
# 	if str_num == str_num[::-1]:
# 		return print(f"NUmber {num} is palindrome number.")
# 	else: 
# 		return print(f"NUmber {num} is not palindrome number.")

# palindrome_check(12121)



# ========================================================================



# Exercise 17. Merging Lists with Parity Filtering
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# def merged_list(list1 ,list2):
# 	if not isinstance(list1, list):
# 		return "Argument must be a list."
# 	if not isinstance(list2, list):
# 		return "Argument must be a list."
	
# 	new_list = [] # Contain odd numbers from the first list and even numbers from the second list


# 	for num in list1:
# 		if num % 2 != 0:
# 			new_list.append(num)
# 	for num in list2:
# 		if num % 2 == 0:
# 			new_list.append(num)

# 	return new_list

# print(f"Result list: {merged_list(list1, list2)}")



# ========================================================================



# Exercise 19. Multi-Tiered Income Tax Calculation

# def income_tax_calc(income):
# 	if income <= 10000:
# 		tax_payable = 0
# 	elif income <= 20000:
# 		# Tax on the first 10k is 0, tax on the rest is 10%
# 		tax_payable = (income - 10000) * 10 / 100
# 	else:
# 		# First 10k: 0%
# 		# Next 10k: 10% tax == 1k
# 		tax_payable = 10000 * 10 / 100
# 		# Remaining income: 20% tax
# 		tax_payable += (income - 20000) * 20 / 100

# 		print(f"Total income tax to pay is {tax_payable}")

# income = int(input("What is your income: "))
# tax_payable = 0
# print("Given income: ", income)

# income_tax_calc(income)



# ========================================================================



# Exercise 20. Nested Loops for Multiplication Tables
# Metrix Generation

# for i in range(1, 11):
# 	for j in range(1, 11):
# 		print(i * j, end="\t")
# 	print(end="\n")



# ========================================================================



# Exercise 21. Downward Half-Pyramid Pattern
# star = "*"
# row = 5
# for i in range(row, 0, -1):
# 	for j in range(0, i):
# 		print(star, end=" ")
# 	print("")



# ========================================================================



# Exercise 22. Custom Exponentiation Function
# This is a built-in operator
# def exponent(base, exp):
# 	return base ** 5

# base = int(input("Base: "))
# exp = int(input("Exponent: "))

# def exponent(base, exp):
# 	num = exp
# 	result = 1

# 	while num > 0:
# 		result *= base
# 		num -= 1

# 	return result

# print(f"{base} raises to the power of {exp} = {exponent(base, exp)}")



# ========================================================================



# Exercise 24. Generate Fibonacci Series
# def fibonacci(term):
# 	start, next = 0, 1

# 	for i in range(0, term):
# 		print(start, end=" ")
# 		result = start + next
# 		start, next = next, result

# fibonacci(5)



# ========================================================================



# Exercise 25. Check Leap Year
# year = int(input("Input any year to check if it is a leap year: "))
# def leap_year(year):
# 	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
# 		return (f'{year} is a leap year.')
# 	else:
# 		return (f'{year} is not a leap year.')
	
# print(leap_year(year))



# ========================================================================



# Exercise 26. Merging Two Dictionaries
# Given Input:
# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "job": "Engineer"}
# #  union operator | to merge two dictionaries effortlessly
# print(dict1|(dict2))



# ========================================================================



# Exercise 27. Finding Common Elements (Intersections)
# Given Input:
# list_a = [1, 2, 3, 4, 5]
# list_b = [4, 5, 6, 7, 8]

# common = list(set(list_a) & set(list_b))

# print(common)



# ========================================================================



# Exercise 28. Odd/Even List Splitter
# Given Input: 
# numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
# even = []
# odd = []

# for i in numbers:
# 	if i % 2 == 0:
# 		even.append(i)
# 	else:
# 		odd.append(i)

# print(f'Even Numbers: {even}')
# print(f'Odd Numbers: {odd}')



# ========================================================================



# Exercise 29. Word Length Analysis
# Given Input: 
# words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# for word in words:
# 	print(f"{word} - {len(word)}")



# ========================================================================



# Exercise 30. Word Frequency Counter (The Histogram)
# Given Input: 
# text = "apple banana apple cherry banana apple"
# words = text.split()
# frequency = {}

# for word in words:
# 	if word in frequency:
# 		frequency[word] += 1
# 	else:
# 		frequency[word] = 1

# print(frequency)



# ========================================================================



# Exercise 31. Print Alternate Prime Numbers
# prime = []
# for num in range(2, 21):
# 	for i in range(2, int((num**0.5)) + 1):
# 		if num % i == 0:
# 			break
# 		prime.append(num)
# print(prime[::2])



# ========================================================================



# Exercise 32. Dictionary of Squares (Mapping Logic)
# result = {}
# for i in range(1, 11):
# 	result[i] = i*i

# print(result)



# ========================================================================



# Exercise 33. Character Replacer (Data Sanitization)
# Given Input: 
# sentence = "I love coding in Python"
# print(sentence.replace(" ", "_"))



# ========================================================================



# Exercise 34. Print Reverse Number Pattern
# row = 5
# for i in range(row, 0, -1):
# 	for j in range(i, 0, -1):
# 		print(j, end=" ")
# 	print(end="")



# ========================================================================



# Exercise 35. Digit Detection in Strings
# Given Input:
# input_string = "Python3"
# contain_digit = False
# for i in list(input_string):
# 	if i.isdigit():
# 		contain_digit = True
# 		break

# print(f"The string '{input_string}' contains a digits: {contain_digit}")



# ========================================================================



# Exercise 36. Capitalize First Letter (Title Case)
# Given Input: 
# text = "hello world from python"
# words = text.split()
# capitalized_words = []

# for word in words:
# 	capitalized_words.append(word.capitalize())
	
# result_text = " ".join(capitalized_words)
# print(result_text)



# ========================================================================



# Exercise 37. Simple Countdown Timer
# start_count = 5

# while start_count > 0:
# 	print(start_count)
# 	start_count -= 1

# print("Blast off!")

# import time

# count = 5
# while count > 0:
# 	print(count)

# 	time.sleep(1)

# 	count -= 1

# print("Blast off!")



# ========================================================================



# Exercise 38. File Creation and Basic I/O
# part 1: writing to the file
# with open("note.txt", "w") as file:
# 	file.write("Hello, this is my first note.\n")
# 	file.write("Python file handling is simple.\n")
# 	file.write("End of file.\n")

# # part 2: reading from the file
# print("Reading file contents: \n")
# with open("note.txt", "r") as file:
# 	content = file.read()
# 	print(content)



# ========================================================================



# Exercise 39. External File Word Counter
# first create sample text file
# with open("sample.txt", "w") as file:
# 	file.write("Coding is the language of the future.")

# # open and count words in the sample file
# try:
# 	with open("sample.txt", "r") as file:
# 		data = file.read()
# 		words = data.split()
# 		print(f"The file contains {len(words)} words.")
# except FileNotFoundError:
# 	print(f"The file named 'sample.txt' was not found.")



# ========================================================================



# Exercise 40. Introduction to Classes (OOP)
# class Car:
# 	def __init__(self, make, model, year):
# 		# setting up attributes
# 		self.make = make
# 		self.model = model
# 		self.year = year

# 	def start_engine(self):
# 		# a method tat uses the object's attributes
# 		print(f"The {self.make} {self.model} {self.year}'s engine is now running!")

# # creating an object (an instance of class)
# my_car = Car("Toyota", "Camry", 2022)

# # calling the method
# my_car.start_engine()
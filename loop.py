# Python Loops Exercises
# Exercise 1. Print first 10 natural numbers using while loop
# ten = 1
# while ten < 11:
# 	print(ten)
# 	ten += 1



# ==========================================================================



# Exercise 2. Display numbers from -10 to -1 using for loop
# for i in range(-10, 0):
# 	print(i)



# ==========================================================================



# Exercise 3. Display a message “Done” after successful execution of for loop
# for i in range(0, 5):
# 	print(i)
# print("Done!")



# ==========================================================================



# Exercise 4. Calculate the sum of all numbers from 1 to N
# num = int(input("Enter number: "))
# current = 0
# for i in range(1, num+1):
# 	current += i
# print(f"Sum is: {current}")



# ==========================================================================



# Exercise 5. Print multiplication table of a given number
# num = int(input("Enter number to get their multiplication: "))
# for i in range(1, 11):
# 	print(num * i)



# ==========================================================================



# Exercise 6. Calculate the cube of all numbers from 1 to a given number
# num = int(input("Enter number: "))
# for i in range(1, num+1):
# 	print(f"Current Number is: {i} and the cube is {pow(i, 3)}")



# ==========================================================================



# Exercise 7. Display numbers from a list using a loop
# Given Input: 
# numbers = [12, 75, 150, 180, 145, 525, 50]

# for num in numbers:
# 	if num % 5 == 0:
# 		if num > 500:
# 			break
# 		if num > 150:
# 			continue
# 		print(num)



# ==========================================================================



# Exercise 8. Count occurrences of a specific element in a list
# list1 = [10, 20, 10, 30, 10, 40, 50, 10, 10, 10]
# target = 10
# count = 0
# for num in list1:
# 	if num == target:
# 		count +=1
# print(f'{target} appears {count} times.')



# ==========================================================================



# Exercise 9. Print elements from a list present at odd index positions
# Given Input: 
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# num = my_list[1::2]
# print(num)

# # OR

# for num in range(1, len(my_list), 2):
# 	print(my_list[num], end=" ")



# ==========================================================================



# Exercise 10. Print list in reverse order using a loop
# Given Input: 
# list1 = [10, 20, 30, 40, 50]
# for i in reversed(list1):
# 	print(i)



# ==========================================================================



# Exercise 11. Reverse a string using a for loop (no slicing)
# Given input:
# word = "Python"
# reverse = ""
# for i in range(len(word) - 1, -1, -1):
# 	reverse += word[i]
# print(f"Original: {word}")
# print(f"Original: {reverse}")



# ==========================================================================



# Exercise 12. Count vowels and consonants in a sentence
# sentence = "Loops are fun!"
# vowels = "aeiou"
# c_count = 0
# v_count = 0

# for char in sentence:
# 	if char.isalpha():
# 		if char in vowels:
# 			v_count += 1
# 		else:
# 			c_count += 1
# print(f"Number of vowels in '{sentence}' is {v_count}")
# print(f"Number of consonant in '{sentence}' is {c_count}")



# ==========================================================================



# Exercise 14. Reverse an integer number
# num = int(input("Enter a number: "))
# reversed_num = 0
# while num > 0:
# 	digit = num % 10
# 	reversed_num = (reversed_num * 10) +digit
# 	num = num // 10

# print(reversed_num)



# ==========================================================================



# Exercise 15. Find largest and smallest digit in a number
# num = 56789
# largest = 0
# smallest = 9

# while num > 0:
# 	digit = num % 10
# 	if digit > largest:
# 		largest = digit
# 	if digit < smallest:
# 		smallest = digit
# 	num = num // 10

# print(f"Larget = {largest}")
# print(f"Smallest = {smallest}")



# ==========================================================================



# Exercise 16. Check if a number is a palindrome
# def check_palindorome(num):
# 	temp = num
# 	reversed_num = 0
# 	while num > 0:
# 		digit = num % 10
# 		reversed_num = (reversed_num * 10) + digit
# 		num = num // 10
	
# 	if reversed_num == temp:
# 		return(print(f'{temp} is palinrome'))
# 	else:
# 		return(print(f'{temp} is not palinrome'))

# check_palindorome(1232)



# ==========================================================================



# Exercise 17. Find factorial of a number
# num = -5
# factrial = 1
# if num < 0:
# 	print("Factorial does not exist for negative number.")
# elif num == 0:
# 	print("Factorial of 0 is 1.")
# else:	
# 	for i in range(1, num+1):
# 		factrial *= i

# 	print(f"Factorial of {num} is {factrial}.")



# ==========================================================================



# Exercise 18. Collatz Conjecture: Generate a sequence until it reaches 1
# num = 9
# print(num, end=" ")
# while num != 1:
# 	if num % 2 == 0:
# 		num = num // 2
# 	else:
# 		num = (3 * num) + 1
# 	print(num, end=" ")



# ==========================================================================



# Exercise 19. Armstrong Number Check
# num = 153
# num_str = str(num)
# power = len(num_str) 
# sum = 0
# for i in num_str:
# 	sum += int(i) ** power

# if sum == num:
# 	print(f"{num} is an armstrong number.")
# else: 
# 	print(f"{num} is not an armstrong number.")



# ==========================================================================



# Exercise 20. Print right-angled triangle Number Pattern using a Loop
# for i in range (1, 6):
# 	for j in range(1, i + 1):
# 		print(j, end=" ")
# 	print('')



# ==========================================================================



# Exercise 22. Print the alternate numbers pattern
# for i in range(1, 20, 2):
# 	print(i, end=" ")



# ==========================================================================



# Exercise 23. Print Alphabet pyramid (A, BB, CCC) pattern
# row = 5
# for i in range (row):
# 	letter = chr(65 + i)
# 	for j in range(i + 1):
# 		print(letter, end=" ")
# 	print("")



# ==========================================================================



# Exercise 24. Hollow square pattern
# size = 5
# for i in range(size):
# 	for j in range(size):
# 		if i == 0 or i == size - 1 or j == 0 or j == size - 1:
# 			print("*", end=" ")
# 		else: 
# 			print(" ", end=" ")
# 	print()



# ==========================================================================



# Exercise 25. Print pyramid pattern of stars
# for i in range(0, 6):
# 	for j in range (i + 1):
# 		print("*", end=" ")
# 	print()
# for i in range(5, 0, -1):
# 	for j in range (i):
# 		print("*", end=" ")
# 	print()



# ==========================================================================



# Exercise 26. Print full multiplication table (1 to 10)
# for i in range(1, 11):
# 	for j in range(1, 11):
# 		print(i * j, end="\t")
# 	print()



# ==========================================================================



# Exercise 27. List Cumulative Sum: Each element is the sum of all previous
# curr_sum = 0
# given = [1, 2, 3, 4]

# cum_sum = []

# for i in given:
# 	curr_sum += i
# 	cum_sum.append(curr_sum)

# print(f"Cumulative Sum: {cum_sum}")



# ==========================================================================



# Exercise 28. Dictionary Filter: Extract pairs where value exceeds a threshold.
# Given Input:
# scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60} 
# threshold = 75
# result = {}

# for name, score in scores.items():
# 	if score >= threshold:
# 		result[name] = score

# print(f"Passing Students: {result}")



# ==========================================================================



# Exercise 29. Find common elements (Intersection) using loop
#  Given input:
# list_a = [1, 2, 3, 4, 5]
# list_b = [4, 5, 6, 7, 8]

# common = []
# for i in list_a:
# 	if i in list_b:
# 		common.append(i)

# print(f"Common elements: {common}")



# ==========================================================================



# Exercise 30. Remove duplicates without set
#  Given inputs
# nums = [1, 2, 2, 3, 4, 4, 4, 5]
# unique_nums = []

# for i in nums:
# 	if i not in unique_nums:
# 		unique_nums.append(i)
# 	# else: continue

# print(f"Unique List: {unique_nums}")



# ==========================================================================



# Exercise 31. Even/Odd Segregation: Move evens to front, odds to back
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = []
# odd = []

# for num in nums:
# 	if num % 2 == 0:
# 		even.append(num)
# 	else: odd.append(num)

# print(f"Segregate List: {even + odd}")



# ==========================================================================



# Exercise 32. List Rotation: Rotate elements left by k positions
# nums = [1, 2, 3, 4, 5]
# k = 2

# for i in range(k):
# 	first_ele = nums.pop(0)
# 	nums.append(first_ele)

# print(nums)



# ==========================================================================



# Exercise 33. Word frequency counter
# Given input
# text = "apple banana apple orange banana apple"
# words = text.split()
# freq = {}

# for word in words:
# 	if word in freq:
# 		freq[word] += 1
# 	else: freq[word]  = 1

# print(freq)



# ==========================================================================



# Exercise 34. Display fibonacci series up to 10 terms
# num1 = 0
# num2 = 1

# for i in range(10):
# 	print(num1, end=" ")
# 	res  = num1 + num2
# 	num1, num2 = num2, res



# ==========================================================================



# Exercise 35. Perfect number check
# num = 28
# divisor_sum = 0

# for i in range(1, (num // 2) + 1):
# 	if num % i == 0:
# 		divisor_sum += i

# if divisor_sum == num:
# 	print(f"{num} is a perfect number.")
# else:
# 	print(f"{num} is not a perfect number.")



# ==========================================================================



# Exercise 36. Binary to decimal conversion using loop
# binary_str = "1110"
# decimal_val = 0

# reversed_binary = binary_str[::-1]

# for i in range(len(reversed_binary)):
# 	if reversed_binary[i] == "1":
# 		decimal_val += 2 ** i
# print(f"Decimal value: {decimal_val}")



# ==========================================================================



# Exercise 37. Display all prime numbers within a range
# for num in range(25, 51):
# 	if num > 1:
# 		for i in range(2, num):
# 			if (num % i) == 0:
# 				break
# 		else:
# 			print(num)



# ==========================================================================



# Exercise 38. Find the sum of the series up to n terms
# start = 2
# total_sum = 0
# num_of_terms = 5

# for num in range(num_of_terms):
# 	total_sum += start
# 	start = start * 10 +2

# print(total_sum)



# ==========================================================================



# Exercise 39. flatten a nested list using loops
# flattened = []
# nested_list = [[10, 20], [30, 40], [50, 60]]

# for num in nested_list:
# 	for i in num:
# 		flattened.append(i)

# print(flattened)



# ==========================================================================



# Exercise 40. Nested list search (2D matrix coordinates)
# matrix = [[10, 20], [30, 40], [50, 60]]
# target = 30

# for row, num in enumerate(matrix):
# 	for col, i in enumerate(num):
# 		if i == target:
# 			print(f"Target {target} found at Row: {row}, Column: {col}")
# 			break
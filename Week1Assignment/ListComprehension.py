# Given a list of numeric strings, convert them into integers. Using List Comprehensions
#Expected output : [1, 2, 3, 4, 5]
strings = ["1", "2", "3", "4", "5"]
integers = [int(s) for s in strings]
print(integers)  


# Extract all integers from a list that are greater than 10. Using List Comprehensions
#Expected output :[13, 16]
numbers = [1, 5, 13, 4, 16, 7]
greater_than_10 = [n for n in numbers if n > 10]
print(greater_than_10)  
# Output: [13, 16]

# Create a list of squares for numbers from 1 to 5. Using List Comprehensions
# Expected output :[1, 4, 9, 16, 25]
squares = [n**2 for n in range(1, 6)]
print(squares)  
# Output: [1, 4, 9, 16, 25]


# Convert a 2D list into a 1D list.Using List Comprehensions
#Expected output : [1, 3, 4, 23, 32, 56, 74, -2, -6, -9]
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
flat_list = [item for row in matrix for item in row]
print(flat_list)  
# Output: [1, 3, 4, 23, 32, 56, 74, -2, -6, -9]

# Given two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3], create a dictionary using dictionary comprehension.
#Expected output : {'a': 1, 'b': 2, 'c': 3}
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)  
# Output: {'a': 1, 'b': 2, 'c': 3}

# Given the dictionary scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}, create a new dictionary containing only the students who scored above 80
#Expected output : {'Alice': 85, 'Charlie': 90}
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
high_scores = {k: v for k, v in scores.items() if v > 80}
print(high_scores)  
# Output: {'Alice': 85, 'Charlie': 90}


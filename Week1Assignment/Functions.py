# Define a function calculate_area that calculates the area of a rectangle and return the result. If no width is provided, it defaults to 10.
def calculate_area(length, width=10):
    return length * width

# Write a recursive function to compute the factorial of a non-negative integer.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Write a function that takes one parameter as a string and reverse it and return.
def reverse_string(s):
    return s[::-1]


# Write a Python function that takes two parameters as lists and to sum all the numbers in a list. 
# a = [8, 2, 3, 0, 7], b =  [3, -2, 5, 1] and return a value.
def sum_two_lists(list1, list2):
    return sum(list1) + sum(list2)

a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1]
result = sum_two_lists(a, b)
print(result)  
# Output: 27


# Write a Python function that takes a list and returns a new list with distinct and sorted elements from the first list. a = [4,1,2,3,3,1,3,4,5,1,7]
def distinct_sorted(lst):
    return sorted(set(lst))

a = [4, 1, 2, 3, 3, 1, 3, 4, 5, 1, 7]
print(distinct_sorted(a))  
# Output: [1, 2, 3, 4, 5, 7]

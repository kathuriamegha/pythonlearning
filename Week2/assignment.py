#-------------lambda,map,filter-------------------------------#

# Given a list let's see how to double each element of the given list. Using map() 
a = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, a))
print(doubled)


# Use filter() and lambda to extract all even numbers from a list of integers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Use reduce() and lambda to find the longest word in a list of strings. from functools import reduce
from functools import reduce
words = ["apple", "banana", "cherry", "date"]
longest_word = reduce(
    lambda a, b: a if len(a) >= len(b) else b,
    words
)
print(longest_word)


# Use map() to square each number in the list and round the result to one decimal place.
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
squared_rounded = list(
    map(lambda x: round(x ** 2, 1), my_floats)
)
print(squared_rounded)

# Use filter() to select names with 7 or fewer characters from the list.
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
short_names = list(filter(lambda name: len(name) <= 7, my_names))
print(short_names)

# Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total_sum = reduce(lambda a, b: a + b, numbers)
print(total_sum)

#---------------------------------All and Any-----------------------#


# Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive. Using all()
numbers = [1, 2, 3, 4, 5]
all_positive = all(n > 0 for n in numbers)
print(all_positive)

# Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()
numbers = [1, 3, 5, 7, 8]
any_even = any(n % 2 == 0 for n in numbers)
print(any_even)

# Determine if any number in a list is divisible by 5 an print.
numbers = [1, 3, 6, 7, 8, 10]
divisible_by_5 = any(n % 5 == 0 for n in numbers)
print(divisible_by_5)


#------------------------Enumerate------------------------------------#

# Using below list and enumerate(), print index followed by value. 
fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)

# Using below dict and enumerate, print key followed by value
person = {"name": "Alice", "age": 30, "city": "New York"}
for _, key in enumerate(person):
    print(f"{key}: {person[key]}")

# Given the list fruits = ["apple", "banana", "cherry", "date", "elderberry"], use enumerate() to create a list of tuples where each tuple contains the index and the corresponding fruit, but only for even indices.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
even_index_fruits = [
    (index, fruit)
    for index, fruit in enumerate(fruits)
    if index % 2 == 0
]
print(even_index_fruits)

#------------------------------------min() and max()--------------------------------#


# Find the Maximum and Minimum Values in a List
numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
max_value = max(numbers)
min_value = min(numbers)
print("Max:", max_value)
print("Min:", min_value)

# Given a set of numbers, find the maximum and minimum values.
setn = {5, 10, 3, 15, 2, 20}
max_value = max(setn)
min_value = min(setn)
print("Max:", max_value)
print("Min:", min_value)

#  Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list, in that order. If there are multiple words of the same shortest or longest length, return the first shortest/longest word found.
def shortest_and_longest(words):
    shortest = min(words, key=len)
    longest = max(words, key=len)
    return shortest, longest
words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
result = shortest_and_longest(words)
print(result)

#----------------------------------------Exception handling-------------------------------------------------------#


# Write a Python program that attempts to divide two numbers a = 10  b = 0
# and handles a ZeroDivisionError if the denominator is zero. Divide a by b and handle the exception and print the error
a = 10
b = 0
try:
    result = a / b
    print(result)
except ZeroDivisionError as e:
    print("Error:", e)


# Apply exception handling to below code and handle an exception if the index is out of range. 
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError as e:
    print("Error:", e)

# Correct this below code with appropriate exception handlings. And finally print “Execution completed”
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error: Invalid input type")
    finally:
        print("Execution completed")
safe_divide(1, 0)
safe_divide(1, "a")

#--------------------Decorator--------------------------------------#

# 1. Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the start and end time. Calculate the total time taken and print.
import time
from functools import wraps
def time_taken(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"Start Time: {start}")
        print(f"End Time: {end}")
        print(f"Total Time Taken: {end - start:.6f} seconds")

        return result
    return wrapper
@time_taken
def append_numbers():
    numbers = []
    for i in range(1, 1001):
        numbers.append(i)
    return numbers
append_numbers()


# 2. Create a parameterised decorator retry that retries a function a specified number of times.
from functools import wraps

def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
            print("All retry attempts failed")
        return wrapper
    return decorator


@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")
    raise ValueError("Random failure")

may_fail("Alice")


# 3. Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.
from functools import wraps

def validate_positive(func):
    @wraps(func)
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be positive")
        return func(x)
    return wrapper
@validate_positive
def square_root(x):
    return x ** 0.5
print(square_root(16))

# 4. Create a decorator cache that caches the result of a function based on its arguments.
	# @cache
    #   	def expensive_computation(x):
    # 		print("Performing computation...")
    # 		return x * x
	
	# expensive_computation(5)
	# expensive_computation(5)

#     Write a cache decorator for it to check if the calculation is already performed then return the result.

from functools import wraps

def cache(func):
    cached_results = {}

    @wraps(func)
    def wrapper(*args):
        if args in cached_results:
            print("Returning cached result...")
            return cached_results[args]

        result = func(*args)
        cached_results[args] = result
        return result

    return wrapper


@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x


print(expensive_computation(5))
print(expensive_computation(5))


# 5. Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access to a function, if a different user then responds “Access denied”.

 	#  def delete_user(user, user_id):
    # 		print(f"User {user_id} deleted by {user['name']}")

	# user1 = {'name': 'Alice', 'permissions': ['admin']}
	# user2 = {'name': John, 'permissions': ['dev']}
	# user3 = {'name': 'Kurt', 'permissions': ['test’']}


from functools import wraps

def requires_permission(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if 'admin' not in user.get('permissions', []):
            print("Access denied")
            return
        return func(user, *args, **kwargs)
    return wrapper


@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")


user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}

delete_user(user1, 101)
delete_user(user2, 102)
delete_user(user3, 103)

#----------------------------------Generator--------------------------------------------------#

# 1. Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers Of 10  numbers 
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci()

for _ in range(10):
    print(next(fib_gen))


# 2. Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.

def infinite_multiples(n):
    multiple = n
    while True:
        yield multiple
        multiple += n


multiples_of_3 = infinite_multiples(3)

for _ in range(5):
    print(next(multiples_of_3))


# 3. Write a generator function called repeat_word(word, times) that yields the given character char a specified number of times.
def repeat_word(word, times):
    for _ in range(times):
        yield word

gen = repeat_word("hello", 5)

for value in gen:
    print(value)


# ------FILE HANDLING---------#

# 1 . Write a Python program to read the entire content of a file named sample.txt and display it.
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


# 2. Write a Python program to count the number of words in a file named words.txt
with open("words.txt", "r") as file:
    content = file.read()
    word_count = len(content.split())

print("Number of words:", word_count)


# 3.Create a program to write the string “Hello, Python!” into a file named output.txt.
with open("output.txt", "w") as file:
    file.write("Hello, Python!")


# 4. Write a Python program to create a CSV file named students.csv with columns Name, Roll Number, and Marks. Add at least three entries

import csv

data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


# 5. From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.

def read_large_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


for line in read_large_file("sample.txt"):
    print(line)


#----------------CLASS-------------------#


# 1. Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Alice", 30)

print(person.name)
print(person.age)


# 2. Problem: Write a Python class named BankAccount with attributes like account_number, balance, and customer_name, and methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount("ACC123", "Bob", 1000)
account.deposit(500)
account.withdraw(300)
account.check_balance()


# 3. Create a class Book with a class method from_string() that creates a Book instance from a string. And print both attributes of the class
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount("ACC123", "Bob", 1000)
account.deposit(500)
account.withdraw(300)
account.check_balance()


# 4. Create a base class Animal with a method sound(). Create subclasses Dog and Cat that overrides the sound() method and call those methods.
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# 5. Write a code to perform multiple inheritance.
class Father:
    def skills(self):
        print("Gardening")


class Mother:
    def skills(self):
        print("Cooking")


class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Coding")


child = Child()
child.skills()


#-------------------------MODULES--------------------------#

# Using datetime, ​​add a week and 12 hours to a date.  Given date: March 22, 2020, at 10:00 AM. print original date time and new date time
from datetime import datetime, timedelta

original_date = datetime(2020, 3, 22, 10, 0)

new_date = original_date + timedelta(weeks=1, hours=12)

print("Original datetime:", original_date)
print("New datetime:", new_date)

# Code to get the dates of yesterday, today, and tomorrow.
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

# Write a code snippet using os module, to get the current working directory and print and create a folder “test”. List all the files and folders in the current working directory and remove the directory “test” that was created.
import os

# Get current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Create directory
os.mkdir("test")
print("Directory 'test' created")

# List files and folders
print("Contents:", os.listdir(cwd))

# Remove directory
os.rmdir("test")
print("Directory 'test' removed")


# Write a Python program to rename a file from old_name.txt to new_name.txt.
import os

os.rename("old_name.txt", "new_name.txt")
print("File renamed successfully")

# Create a file and Write a Python program to get the size of a file named example.txt 
import os

with open("example.txt", "w") as file:
    file.write("Hello World")
size = os.path.getsize("example.txt")
print("File size:", size, "bytes")


# Convert the string "Feb 25 2020 4:20PM" into a Python datetime object
from datetime import datetime

date_str = "Feb 25 2020 4:20PM"

dt = datetime.strptime(date_str, "%b %d %Y %I:%M%p")

print(dt)


# Subtract 7 days from the date 2025-02-25 and print the result.
from datetime import datetime, timedelta

date_val = datetime(2025, 2, 25)
new_date = date_val - timedelta(days=7)

print("New date:", new_date.date())


# Format the date 2020-02-25 as "Tuesday 25 February 2020"
from datetime import datetime

date_val = datetime(2020, 2, 25)

formatted_date = date_val.strftime("%A %d %B %Y")

print(formatted_date)

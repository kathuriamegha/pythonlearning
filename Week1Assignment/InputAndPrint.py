# Objective: Ask the user for their name and greet them.
# Task: Write a program that asks the user for their name and then prints a greeting   message using their name.

name = input("Enter your name: ")
print("Hello, " + name + "! Welcome!")


# Objective: Perform basic arithmetic operations based on user input.
# Task: Ask the user to enter two numbers from the user and print their sum, multiplication, and division.

# Ask the user for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
sum_result = num1 + num2
mul_result = num1 * num2
div_result = num1 / num2

# Print results
print("Sum:", sum_result)
print("Multiplication:", mul_result)
print("Division:", div_result)


# Task: Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print.
names_input = input("Enter names separated by commas: ")
print("Names list:", names_input.split(","))

# Task: Ask the user to enter their age and check if they are eligible to vote based on their age.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are NOT eligible to vote.")


# Task: For value = 3.14159, Using f-string print output for only up to 2 decimal places.
value = 3.14159
print(f"{value:.2f}")

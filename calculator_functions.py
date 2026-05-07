# File Name: calculator_functions.py

# Python Function Program

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

# Main Program
num1 = 20
num2 = 5

print("----- CALCULATOR USING FUNCTIONS -----")

print("Addition :", add(num1, num2))
print("Subtraction :", subtract(num1, num2))
print("Multiplication :", multiply(num1, num2))
print("Division :", divide(num1, num2))

# Function with loop
def display_numbers():
    print("\nNumbers from 1 to 5")
    
    for i in range(1, 6):
        print(i)

display_numbers()

# Even or Odd Function
def check_even_odd(number):
    if number % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

print("\nChecking Number")
print(check_even_odd(17))

print("\nProgram Executed Successfully")

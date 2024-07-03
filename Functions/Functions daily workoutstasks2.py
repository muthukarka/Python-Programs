# Define the functions for each operation
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
        return "Error! Division by zero."

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add / subtract / multiply / divide): ").strip().lower()

# Perform the relevant operation
if operation == "add":
    result = add(num1, num2)
elif operation == "subtract":
    result = subtract(num1, num2)
elif operation == "multiply":
    result = multiply(num1, num2)
elif operation == "divide":
    result = divide(num1, num2)
else:
    result = "Invalid operation."

# Print the result
print("The result is:", result)

def greet(name="User", message="Welcome"):
    print(message, name)

# 2. Func using keyword arguments
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Division by zero not allowed"
        return a / b
    else:
        return "Invalid operation"

def perform_operation(func, x, y):
    return func(x, y)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y


# Main program
print("Default Parameters:")
greet()
greet("Sejal")
greet(message="Hello", name="Sejal")

print("\nKeyword Arguments:")
print("Addition:", calculate(15, 5))
print("Subtraction:", calculate(15, 5, operation="subtract"))
print("Multiplication:", calculate(a=15, b=5, operation="multiply"))

print("\nPassing Function as Argument:")
print("Add:", perform_operation(add, 9, 3))
print("Multiply:", perform_operation(multiply, 9, 3))
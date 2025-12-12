a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
addition = a + b
subtraction = a - b
multiplication = a * b
if b != 0:
    division = a / b
else:
    division = "Undefined (cannot divide by zero)"
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

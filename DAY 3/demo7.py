def factorial(n):
    if n == 0 or n == 1:      
        return 1
    else:
        return n * factorial(n - 1)

def power(base, exp):
    if exp == 0:             
        return 1
    else:
        return base * power(base, exp - 1)


# Main program
num = int(input("Enter a number for factorial: "))
print("Factorial of", num, "is:", factorial(num))

base = int(input("\nEnter base: "))
exp = int(input("Enter exponent: "))
print(base, "raised to the power", exp, "is:", power(base, exp))
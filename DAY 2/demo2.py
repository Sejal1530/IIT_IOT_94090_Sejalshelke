num = int(input("Enter a 5 digit number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Check after reversing the complete number
if original == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
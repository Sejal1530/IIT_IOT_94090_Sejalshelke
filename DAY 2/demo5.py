def print_binary(num):
    if num == 0:
        print(0)
        return

    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2

    print("Binary representation:", binary)
n = int(input("Enter a number: "))
print_binary(n)
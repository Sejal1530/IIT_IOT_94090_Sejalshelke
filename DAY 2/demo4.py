def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(start, end):
    print("Prime numbers in the given range are:")
    for n in range(start, end + 1):
        if is_prime(n):
            print(n, end=" ")

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print_primes(start, end)
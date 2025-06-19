# Input number
num = 17

# Assume number is prime
is_prime = True

# Check for factors from 2 to num-1
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

# Output result
if is_prime and num > 1:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

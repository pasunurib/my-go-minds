def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True

given_number = 85647

if is_prime(given_number):
    print(f"{given_number} is a Prime Number.")
else:
    print(f"{given_number} is  not a prime number")

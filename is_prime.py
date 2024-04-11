def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_numbers(minimum, maximum):
    prime_num = []
    for num in range(minimum, maximum + 1):
        if is_prime(num):
            prime_num.append(num)
    return prime_num

minimum = 1
maximum = 50
print(prime_numbers(minimum, maximum))

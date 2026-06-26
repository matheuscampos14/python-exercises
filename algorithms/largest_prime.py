def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        print(num, i, num % i == 0)
        if num % i == 0:
            return False
    return True

def largest_prime(n):
    for num in range(n - 1, 1, -1):
        if is_prime(num):
            return num
    return None
print(largest_prime(20))
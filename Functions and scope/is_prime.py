import math


def is_prime(num):
    square_root = math.floor(num**0.5)
    for i in range(2, square_root+1):
        if num % i == 0:
            return False
    return True

print(is_prime(4))

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
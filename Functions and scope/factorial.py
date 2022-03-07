def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

def factorial_recursive(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_recursive(n - 1)


# testing
for n in range(1, 6):  
    print(n, factorial_recursive(n))


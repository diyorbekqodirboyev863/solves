def is_prime(n):
    """
    Checks if a given number is prime.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_primes(n):
    """
    Generates a list of all prime numbers up to a given number.
    
    Args:
        n (int): The upper limit for the prime numbers.
    
    Returns:
        list: A list of all prime numbers up to the given number.
    """
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

# Check if a number is prime
print(is_prime(7))  # True
print(is_prime(12))  # False

# List all primes up to a given number
print(list_primes(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
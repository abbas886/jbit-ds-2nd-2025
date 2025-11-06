
# definition of the method
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b    

def multiply_numbers(a, b):
    return a * b
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b    

# giving number is prime or not
# list the prime numbers in a given range  - nexted loops - without using nested loops, you should able t
# reuse the is_prime function

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return True 
def list_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes





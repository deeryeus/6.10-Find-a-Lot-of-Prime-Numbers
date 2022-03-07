#function returns if number is prime
def is_prime(x):

    prime = True
    n = 1

    if x == 1: #1 is not a prime number
        return False

    while n in range(1, x): 
        if x % n == 0 and n > 1 and n < x: 
            prime = False
        n += 1
    
    return prime

#function returns primes below inputted number
def primes_below(x):

    i = 1
    primes_list = []

    for i in range(1, x):
        if is_prime(i) == True:
            primes_list.append(i)
        i += 1

    return primes_list


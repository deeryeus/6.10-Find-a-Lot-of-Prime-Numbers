#function returns if number is prime
def list_primes(x):
    n = 1
    primes_list = []
    while n in range(1, x): 
        if x % n == 0 and n > 1 and n < x:  
            primes_list.append(n)
        n += 1
    print(primes_list)


        
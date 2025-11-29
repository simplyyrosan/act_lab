def is_prime(n):
    a = "is prime"
    for i in range(2, n):
        if n%i==0:
            a = "is not prime"
            break
    print(n, a)
    
    
is_prime(5)
        

def is_prime(n):
    a = "is prime"
    for i in range(2, n):
        if n%i==0:
            a = "is not prime"
            break
    print(n, a)

#main 
n = int(input("Enter a number: "))
is_prime(n)
        

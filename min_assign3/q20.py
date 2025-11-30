def is_perfect(n):
    sum=0
    for i in range(1, n):
        if n%i==0:
            sum+=i
    if sum==n:
        print("Perfect")
    else:
        print("Not perfect")
        
#
n = int(input("Enter a number: "))
is_perfect(n)
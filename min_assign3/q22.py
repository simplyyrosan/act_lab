def digital_root(n):
    while n>10:
        sum = 0
        while n>0:
            sum+=n%10
            n//=10
        n = sum
    return n
    
num = int(input("Enter a numner: "))
print(digital_root(num))

            

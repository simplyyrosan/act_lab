n =  int(input("Enter a number: "))
num = n
sum = 0
while n:
    sum += n%10
    n = n//10 
    
print(f"The sum of the digits of {num} is",sum)
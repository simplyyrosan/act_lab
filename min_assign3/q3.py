n =  int(input("Enter a number: "))
sum = 0
while n:
    sum += n%10
    n = n//10 
    
print(sum)
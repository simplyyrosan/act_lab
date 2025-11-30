
n = int(input("Enter value for 'n': "))
sum= 0
x= int(input("Enter value for 'x': "))
a = -1
for i in range(1, n+1, 2):
    fac = 1
    for j in range(1, i+1):
        fac*=j
    
    a *= -1
    sum += a*(x**i/fac)
    
print(sum)


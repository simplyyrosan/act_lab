
n = 7
sum= 0
x=1.57
a = -1
for i in range(1, n+1, 2):
    fac = 1
    for j in range(1, i+1):
        fac*=j
    
    a *= -1
    #print(i, x, fac, a)
    sum += a*(x**i/fac)
    
print(sum)

#math.pow(i, 3)
#i**3
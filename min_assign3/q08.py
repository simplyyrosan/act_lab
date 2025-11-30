n = 5
for i in range(1, n+1):
    print("*"*i, end="")
    print(" "*((n-i)*2), end="")
    print("*"*i)
for j in range(n-1, 0, -1):
    print("*"*j, end="")
    print(" "*((n-j)*2), end="")
    print("*"*j)

#2 8 i=1 space n*2-2*i 
#(n-i)*2
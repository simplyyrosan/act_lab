n = int(input("Enter a number: "))

for i in range(1, n+1):
    if i%2==0:
        i = i*(-1)
    print(i, end=" ")

#or ----------------------------------

n =  int(input("Enter a number: "))

a = -1
for i in range(1, n+1):
    a = a*(-1)
    print(i*a, end = " ")
n=5
for i in range(n):
    print(" "*(n-i), end="") #This prints spaces
    for j in range(1,i+1): #  1 12 123
        print(j, end="")
    for k in range(i+1, 0, -1): #1 21 321 4321 
        print(k, end="")
    print()

#i = 0
#5 
#
#1
#i = 1
#4 
#1
#21
#i = 2
#3
#12
#321

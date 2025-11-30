min = int(input("Enter the minimum range: "))
max = int(input("Enter the maximum range: "))
print("Even number within the range are: ")
for i in range(min, max+1):
    if i%2==0:
        print(i, end = " ")
            
a = eval(input("Input: "))

for i in range(len(a)):

    if i+1 < len(a):
        if a[i]+1 != a[i+1]:
            print(a[i]+1, "is missing")
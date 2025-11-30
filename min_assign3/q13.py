a = [2, 3, 4, 6, 8, 10]

for i in range(len(a)):

    if i+1 < len(a):
        if a[i]+1 != a[i+1]:
            print(a[i]+1, "is missing")

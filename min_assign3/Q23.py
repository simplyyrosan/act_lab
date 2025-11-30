s = input("Enter a string: ")
l = s.split()

x = ""
for i in l:
    if len(i) > len(x):
        x = i 

print(x, "is the longest word.")


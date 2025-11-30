def gcd(a, b):
    while b>0:
        temp = b
        b = a%b
        a = temp
    return a

#Main
x = int(input("Enter first num: "))
y = int(input("Enter second num: "))
print(f"GCD of {x} and {y} is", gcd(x, y))

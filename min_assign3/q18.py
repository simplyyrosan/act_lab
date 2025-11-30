def is_palindrome(s):
    temp = s
    rev = 0
    while temp>0:
        d = temp%10
        rev = rev*10 + d
        temp = temp//10
    return rev==s
    
n = int(input("Enter a number: "))
if is_palindrome(n):
    print(n, "is a Palindrome") 
else:
    print(n, "is not a Palindrome") 
    
def is_anagram(a, b):
    a = a.lower()
    b = b.lower()
    return sorted(a) ==  sorted(b)
    
#Main body
s1 = input("Enter first word: ")
s2 = input("Enter second word: ")

if is_anagram(s1, s2):
    print("Its an anagram")
else:
    print("Its not an anagram")
def count_vc(s):
    v = 0
    c = 0
    for i in s:
        if i.lower() in "aeiou":
            v+=1
        elif i.lower() in "bcdfghjklmnpqrstvwxyz":
            c+=1
    return v, c

#Main
t = input("Enter a string: ")
vc = count_vc(t)
print(f"vowels: {vc[0]}, consonant: {vc[1]}" )
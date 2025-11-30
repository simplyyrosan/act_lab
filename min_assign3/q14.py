'''
#Factorial Calculation 
n = 5 
fact = 0 <-- Logical Error, fact should be 1
for i in range(1, n+1)   <-- Syntax Error ':' missing
    fact = fact*i
    print("Factorial =", fact) <-- Indentation error Or Logical Error

'''

#Fixed code --->

#Factorial Calculation 
n = 5 
fact = 1
for i in range(1, n+1):
    fact = fact*i
print("Factorial =", fact) 
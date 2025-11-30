'''
num_sudents = int(input("Enter number of students: "))
for i in range(num_sudents):
name = input("Enter name: ") <-- Indentation 
marks = input("Enter marks: ") <-- int(input()) cause entering the marks + Indentation
if marks > 50   <---- ':' colons missig
print(name, "Passed") <-- double Indentation (inside if-block)
else: <-- Indentation
print(name, "Failed") <-- double Indentation (inside else-block)
total = total + marks <-- Intialization of total out side loop + Identation
average = total / num_sudents
print("Average marks = " + average) <--- Can't add String with num
'''

#Fixed code ---->

num_sudents = int(input("Enter number of students: "))
total = 0  #Intialization of total
for i in range(num_sudents): 
    name = input("Enter name: ")
    marks = int(input("Enter marks: ")) #added int()
    if marks > 50: #Added ':'
        print(name, "Passed") 
    else:
        print(name, "Failed")
    total = total + marks

average = total / num_sudents
print("Average marks = " + str(average)) #or print("Average marks =", average)
import random

r = random.randint(1, 100)

for i in range(5):
    n = int(input("Enter your guess (1-100): "))
    if n==-1: 
        print("You choose to quit")
        break
    else:
        if n==r:
            print("You win!!")
            break
        if n>r:
            print("too high")
        elif n<r:
            print("too low")
else:
    print("You lose!!\n", r, "was the correct number")
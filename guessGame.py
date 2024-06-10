from random import randint
while True:
    try:
        a= input("enter the lower limit")
        b= input("enter the upper limit")
        break
    except ValueError:
        print("not a valid number, try again")
print(a, b)

rndInt= randint(a,b)
n= int(input("enter a number between 0 & 100"))

while(n!=rndInt):
    print("enter your guess")
    temp= int(input())
    d= rndInt
from math import *
n=int(input("Enter a number to check for prime number : "))
if(n==0): print("Not a prime number")
i=1
for i in range(1,int(sqrt(n))+1):
    if(n%i==0):
        i=0
if(i): print("It's Prime")
else: print("Not a Prime Number")
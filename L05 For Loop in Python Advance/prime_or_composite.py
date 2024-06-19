from math import *
def main():
    n=int(input("Enter a number : "))
    flag=True
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            flag=False
            break
    if(flag):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is a composite number")


if __name__=="__main__":
    main()
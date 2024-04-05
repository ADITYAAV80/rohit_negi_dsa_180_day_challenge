def factors(n:int):
    i=0
    print("factors of the numbers are : ")
    while(i<n//2):
        i+=1
        if(n%i==0):
            print(i,end=" || ")
    print(n)


if __name__=="__main__":
    n=int(input("Enter a number to find factors : "))
    factors(n)
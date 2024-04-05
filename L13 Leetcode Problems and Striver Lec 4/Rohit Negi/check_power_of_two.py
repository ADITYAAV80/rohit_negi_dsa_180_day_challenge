def isPowerOfTwo(n: int):
    flag= True
    if(n<=0):
        return False
    else:
        while(n>1):
            if(n%2!=0):
                flag=False
            n=n//2
        return flag

if __name__ == '__main__': 
    t = int (input("Enter the number : "))
    sol=isPowerOfTwo(t)
    if(sol): print("Yes, it's power of two")
    else: print("No, it's not power of two")

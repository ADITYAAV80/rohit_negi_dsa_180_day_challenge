def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    a=[]
    while(x!=0):
        a.append(x%10)
        x=x//10
    if len(a)==1:
        return True
    else:
        flag=True
        for i in range(0,len(a)//2):
            if a[i]!=a[len(a)-i-1]:
                flag=False
    return flag

if __name__=="__main__":
    n=int(input("Enter a number to reverse : "))
    y=isPalindrome(n)
    print("Is your number a palindrome?",y)
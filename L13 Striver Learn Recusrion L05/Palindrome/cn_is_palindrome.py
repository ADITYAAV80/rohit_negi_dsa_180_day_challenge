def isPalindrome(string: str) -> bool:
    flag= True
    n=len(string)
    if(n==0 or n==1):
       return flag
    if(string[0:1]==string[n-1:n]):
        flag=isPalindrome(string[1:n-1])
        return flag
    else:
        return False

if __name__ == '__main__': 
    t =input ("Enter the string to check for palindrome : ")
    sol=isPalindrome(t)
    if sol:
        print("Yes, It's a palindrome")
    else:
        print("No, not a palindrome")

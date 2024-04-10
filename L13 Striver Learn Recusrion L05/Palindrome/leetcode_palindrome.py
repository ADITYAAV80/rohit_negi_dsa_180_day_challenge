
def isPalindrome(s: str) -> bool:
    i=0
    j=len(s)-1
    while(i<j):
        if s[i].isalnum()==False:
            i+=1
        elif s[j].isalnum()==False:
            j-=1
        elif s[i].lower()==s[j].lower():
            i+=1
            j-=1
        else:
            return False
    return True

if __name__ == '__main__': 
    t = input ("Enter the string to check for palindrome : ")
    sol=isPalindrome(t)
    if sol:
        print("Yes, It's a palindrome")
    else:
        print("Not a Palindrome")
n=int(input("Enter a number to check for palindrome"))  
# taking n as a input 
## write your code 
a=[]
while(n!=0):
    a.append(n%10)
    n=n//10

if len(a)==1:
    print("true")
else:
    flag=True
    for i in range(0,len(a)//2):
        if a[i]!=a[len(a)-i-1]:
            flag=False
    if(flag):
        print("true")
    else:
        print("false")


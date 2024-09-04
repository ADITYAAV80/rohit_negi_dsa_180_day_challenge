def calcroot(m,n,num):    
    temp = 1
    for i in range(n):
        temp*=m
        if temp>num:
            return 2
    if temp<num:
        return 0
    else:
        return 1

def nthroot(num,n):
    l,r=0,num
    ans =-1
    while(l<=r):
        m=(l+r)//2
        val = calcroot(m,n,num)
        print(val,m)
        if val==1:
            ans = m
            break
        if val==2:
            r=m-1
        else:
            l=m+1
    return ans
            

if __name__ == "__main__":
    num = int(input("Enter the number you want nth root of : "))
    n = int(input("Enter value of n : "))
    print("The integer root of number is :", nthroot(num,n))
def majority_el(arr:list):
    n=len(arr)
    count1,count2,me1,me2=0,0,-65535,-65535
    for i in range(n):
        if count1==0 and arr[i]!=me2:
            count1=1
            me1=arr[i]
        elif count2==0 and arr[i]!=me1:
            count2=1
            me2=arr[i]
        elif arr[i]==me1:
            count1+=1
        elif arr[i]==me2:
            count2+=1
        else:
            count1-=1
            count2-=1
    total1,total2,treshhold=0,0,round(n//3)
    ans=[]
    for i in range(n):
        if arr[i]==me1:
            total1+=1
            if total1>treshhold:
                ans.append(me1)
                break
    for i in range(n):
        if arr[i]==me2:
            total2+=2
            if total2>treshhold:
                ans.append(me2)
                break
    return ans


if __name__=="__main__":
    arr=list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    sol=majority_el(arr)
    print("The Majority elements are :",sol)
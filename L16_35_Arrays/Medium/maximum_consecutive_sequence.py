def maximum_consecutive_element(arr,n):
    ans=set()
    maxlen=0
    for i in arr:
        ans.add(i)
    for i in ans:
        if i-1 not in ans:
            element=i
            length=1
            while element+1 in ans:
                length+=1
                element+=1
            maxlen=max(maxlen,length)
    return maxlen

if __name__=="__main__":
    arr=list(map(int,input("Enter array elements seperated by space: ").split(" ")))
    sol=maximum_consecutive_element(arr,len(arr))
    print("Length of maximum consecutive sequence is : ",sol)
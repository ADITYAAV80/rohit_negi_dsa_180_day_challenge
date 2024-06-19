def merge(arr: list,l: int,m: int,r: int):
    temp=[]
    left,right=l,m+1
    while(left<=m and right<=r):
        if(arr[left]<=arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while(left<=m):
        temp.append(arr[left])
        left+=1
    while(right<=r):
        temp.append(arr[right])
        right+=1  
    for i,val in enumerate(temp):
        arr[l+i]=val
    return arr

def mergesort(arr :list,l: int,r: int):
    if(l>=r):
        return
    m=(l+r)//2
    mergesort(arr,l,m)
    mergesort(arr,m+1,r)
    merge(arr,l,m,r)



if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    mergesort(arr,0,len(arr)-1)
    for i in arr:
        print(i,end=" ")
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

def countrevpairs(arr,l,m,r):
    count = 0
    left,right = l,m+1
    while left<=m:
        while right<=r and arr[left]>2*arr[right]:
            right+=1
        count+=right-(m+1)
        left+=1
    return count


def partition(arr :list,l: int,r: int):
    count=0
    if(l<r):
        m=(l+r)//2
        count+=partition(arr,l,m)
        count+=partition(arr,m+1,r)
        count+=countrevpairs(arr,l,m,r)
        merge(arr,l,m,r)
    return count


if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    sol=partition(arr,0,len(arr)-1)
    print("No of reverse pairs:",sol)
    
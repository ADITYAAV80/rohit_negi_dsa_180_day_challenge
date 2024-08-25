count=0
def bin_search(arr,x):
    n = len(arr)
    l,r = 0,n-1
    while(l<=r):
        m=(l+r)//2
        print(l,"+",r,"//2=",m,arr[m])
        if arr[m]>x:
            print("r=",m-1)
            r=m-1
            ans=m
            print("ans",ans)
        else:
            print("l=",m+1)
            l=m+1
        print()

bin_search([1,2,3,3,7,8,9,9,9,11],9)

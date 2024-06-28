def alt_pos_and_neg(arr):
    posindex,negindex=0,1
    ans=[0]*len(arr)
    for i in range(0,len(arr)):
        if arr[i]>=0:
            ans[posindex]=arr[i]
            posindex+=2
        else:
            ans[negindex]=arr[i]
            negindex+=2
    return ans

if __name__=="__main__":
    arr=list(map(int,input("Enter array elements seperated by space: ").split(" ")))
    sol=alt_pos_and_neg(arr)
    print("Array with alternate positive and negative elements: ",sol)
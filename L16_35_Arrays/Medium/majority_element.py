def majority_element(arr):
    count,counter=0,0
    for i in range(0,len(arr)):
        if count==0:
            element=arr[i]
            count=1
        elif arr[i]==element:
            count+=1
        else:
            count-=1
    for i in range(0,len(arr)):
        if arr[i]==element:
            counter+=1
        if counter>(len(arr)//2):
            return element
    return "Does not exist"

if __name__=="__main__":
    arr=list(map(int,input("Enter array elements seperated by space: ").split(" ")))
    sol=majority_element(arr)
    print("Majority element : ",sol)
def merge_overlap_subinterval(intervals):
    n = len(intervals)
    i = 0
    sol=[]
    while i<n:
        if not sol:
            sol.append(intervals[i])

        elif intervals[i][0]<=intervals[i-1][1]:
             if intervals[i][1]>sol[-1][1]:
                  sol[-1][1]=intervals[i][1]
        else:
            sol.append(intervals[i])
        i+=1
    return sol

if __name__=="__main__":
    n = int(input("Enter the number of subinterval : "))
    nums=[]
    for i in range(n):
            arr=[]
            arr=list(map(int,input(f'enter subinterval {i+1} :').split(" ")))
            nums.append(arr)
    sol = merge_overlap_subinterval(nums)
    print("The modified subintervals are:",sol)
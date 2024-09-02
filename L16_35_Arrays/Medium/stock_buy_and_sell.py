def stock_buy_and_sell(arr):

    minval,profit = float('inf'),0
    for i in range(0,len(arr)):
        minval = min(minval,arr[i])
        profit = max(profit,arr[i]-minval)
    return profit



if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    sol=stock_buy_and_sell(arr)
    print("The max profit is :",sol)
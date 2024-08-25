def main(n:int):
    for row in range(1,n+1):
        result=1
        print(result,end=" ")
        for col in range(1,row):
            result*=(row-col)
            result//=col
            print(result,end=" ")
        print()


if __name__=="__main__":
    n=int(input("Enter number of rows"))
    main(n)

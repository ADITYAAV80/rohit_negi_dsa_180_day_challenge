def sum(a,b):
    print(a+b)

def main():
    lis=list(map(int,input("Enter Two Numbers : ").split(" ")))
    a=lis[0]
    b=lis[1]
    sum(a,b)

if __name__=="__main__":
    main()
def break_or_continue(n:int, a:int):
    i=0
    print("break :")
    while(i!=n):
        i+=1
        if(i==a):
            break
        print(f"{i},",end="")
    i=0
    print("\ncontinue :")
    while(i!=n):
        i+=1
        if(i==a):
            continue
        print(f"{i},",end="")


if __name__=="__main__":
    n=int(input("Enter a number to print n numbers : "))
    a=int(input("Enter a number to break or continue : "))
    break_or_continue(n,a)
def compare(a,b):
    if a>b:
        print("{} is greater".format(a))
    elif b>a:
        print(f"{b} is greater")
    else:
        print("both",a,"and "+str(b)+" are equal")

if __name__=="__main__":
    a=int(input("enter first number:\t"))
    b=int(input("enter second number:\t"))
    compare(a,b)
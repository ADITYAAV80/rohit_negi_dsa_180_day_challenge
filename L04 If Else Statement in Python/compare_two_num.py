def compare(a,b):
    if a>b:
        print("{} is greater".format(a))
    elif b>a:
        print(f"{b} is greater")
    else:
        print("Both",a,"and "+str(b)+" are equal")

if __name__=="__main__":
    a=int(input("Enter first number:\t"))
    b=int(input("Enter second number:\t"))
    compare(a,b)
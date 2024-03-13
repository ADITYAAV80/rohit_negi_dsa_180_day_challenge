def pos_or_neg(a):
    if a>=0:
        print(f"{a} is +ve")
    elif a<0:
        print(f"{a} is -ve")


if __name__=="__main__":
    a=int(input("enter a number:\n"))
    pos_or_neg(a)
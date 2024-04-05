
def multiplication_table(n:int):
    i=0
    while(i<10):
        i+=1
        print(n,"*",i,"=",(n*i),end=" || ")




if __name__=="__main__":
    n=int(input("Enter a number for multiplication table : "))
    multiplication_table(n)
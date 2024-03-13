def grade():
    a = int(input("enter your marks out of 100\n"))
    if(a>90 and a<=100):
        print("A+")
    elif(a>80 and a<=90):
        print("A-")
    elif(a>70 and a<=80):
        print("B+")
    elif(a>60 and a<=70):
        print("B-")
    elif(a>50 and a<=60):
        print("C+")
    elif(a>40 and a<=50):
        print("C-")
    elif(a>33 and a<=40):
        print("D")
    else:
        print("fail")    


if __name__=="__main__":
    grade()
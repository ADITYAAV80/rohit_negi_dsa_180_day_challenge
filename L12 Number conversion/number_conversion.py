def convert_base_less_than_10_num(n:int, inp :int):
    
    """input to decimal"""
    decimal=0
    i=0
    while(n!=0):
        x=n%10
        decimal+=x*pow(inp,i)
        n=n//10
        i+=1
    return decimal

def convert_base_16_num(num :str,inp :int):
    output=[]
    decimal=0
    for i in range(len(num)-1,-1,-1):
        output.append(num[i])
    hex_to_x={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    i=len(output)-1
    while(i>=0):
        if(ord(output[i])>=65):
            decimal+=pow(16,i)*hex_to_x[output[i]]
        else:
            decimal+=pow(16,i)*output[i]
        i-=1
    return decimal

def decimal_to_output(decimal:int, out:int):
    output=[]
    if out<=10:
        """decimal to output"""
        while(decimal!=0):
            x=decimal%out
            output.append(x)
            decimal=decimal//out
        """printing output"""
        i=len(output)-1
        print("Output is (",end="")
        while(i>=0):
            print(output[i],end="")
            i-=1
        print(f"){out}",end="")
    elif out==16:
        x_to_hex={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
        while(decimal!=0):
            x=decimal%out
            output.append(x)
            decimal=decimal//out
        i=len(output)-1
        print("Output is (",end="")
        while(i>=0):
            if(output[i]<=9):
                print(output[i],end="")
            else:
                print(x_to_hex[output[i]],end="")
            i-=1
        print(f"){out}",end="")
    else:
        print("invalid output base number")



if __name__=="__main__":
    inp=int(input("Enter the base of input number format(1-10/16) : "))
    if inp<=10:
        num=int(input("Enter the number : "))
        out=int(input("Enter the base of output number format(1-10/16) : "))
        decimal=convert_base_less_than_10_num(num,inp)
        decimal_to_output(decimal,out)
    elif inp==16:
        num=str(input("Enter the number : "))
        out=int(input("Enter the base of output number format(1-10/16) : "))
        decimal=convert_base_16_num(num,inp)
        decimal_to_output(decimal,out)
    else:
        print("invalid input")
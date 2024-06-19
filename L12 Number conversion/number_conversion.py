def decimal_to_ans(n:str, inp_base :int, out_base:int):
    
    """input to decimal"""
    l=list(n)
    dec=0
    for i in l:
        if i.isnumeric()==1:
            dec=dec*inp_base+int(i)
        if i.isalpha()==1:
            dec=dec*inp_base+ord(i)-55

    """decimal to output"""
    a=""
    while(dec>0):
        x=dec%out_base
        if(x<9):
            a+=str(x)
        else:
            a+=chr(65+x-10)
        dec=dec//out_base
    return a[::-1]

if __name__=="__main__":
    num=str(input("Enter Number : "))
    base_input=int(input("Enter Base of the input : "))
    base_output=int(input("Enter Base of the ouput : "))
    ans=decimal_to_ans(num,base_input,base_output)
    print("Your Solution is : ",ans)
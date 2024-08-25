class stack:
    def __init__(self,size):
        self.top=-1
        self.data=[]
        self.size=size

    def push(self,element):
        self.top+=1
        if self.top>=self.size:
            self.top=self.size-1
            print("Stack Overflow")
            return
        self.data.append(element)        

    def pop(self):
        self.top-=1
        if self.top<-1:
            self.top=-1
            print("Stack Underflow")
            return
        return self.data.pop()
    
    def tos(self):
        if self.top<0:
            print("Stack is Empty")
            return
        return self.data[self.top]
    
    def empty(self):
        for i in range(0,self.top):
            self.data.pop()
        self.top=-1

    def len(self):
        return self.top+1
    
    def print(self):
        for i in range(self.top,0,-1):
            print("|",self.data[i],"|")
        print("|",self.data[-1],"|",end="\n")
        print("-----")

if __name__=="__main__":
    y=stack(5)
    #to check push functions
    for i in range(0,5):
        y.push(i+1)
    y.print()
    #to test stack overflow
    y.push(6)
    #check length function
    print(y.len())
    #to check pop functions
    for i in range(0,5):
        print(y.pop())
    print(y.len())
    #to check top of stack function
    print(y.tos())
    for i in range(0,3):
        y.push(i+1)
    y.print()
    print(y.tos())
    #to check empty function
    y.empty()
    y.push(1)
    y.print()
    print(y.len())
class array:
    def __init__(self,size):
        self.size=size
        self.data=[None]*self.size

    def __repr__(self):
        datastr="["
        for i in range(0,self.size-1):
            datastr+=str(self.data[i])+","
        datastr+=str(self.data[self.size-1])+"]"
        return datastr

    def add(self,index,element):
        self.data[index]=element

    def remove(self,index):
        self.data[index]=None

    def getitem(self,index):
        if index>=0 and index<self.size:
            return self.data[index]
        return "Index not Valid"
    
    def len(self):
        return self.size

if __name__=="__main__":
    x=array(10)
    #inserting into array
    for i in range(0,x.len()):
        x.add(i,3*(i+1))
    #printing array to check __repr__,insertion
    print(x)
    #to check if remove  function is working as intended
    x.remove(5)
    print(x)
    #to test getitem functions
    print(x.getitem(9))
    print(x.getitem(10))
n=20
x=25
print("outside the block:",x)

def func():
    print("function n :",n)

def global_and_local():
    y=100
    print("inside the global_and_local y (local variables can be accessed within local):",y)
    print("inside the global_and_local x (global varibales can be accessed inside local):",x)

"""throws error""" 
def can_i_access_y_outside_global_and_local_function():
    print("y :",y)

if __name__=="__main__":
    """Comment the below line to see difference"""
    n=10 
    print("main n :",n)
    func()
    n=30
    func()
    global_and_local()
    """uncomment out below line for scope error"""
    """can_i_access_y_outside_global_and_local_function()"""

"""uncomment out below line for scope error"""
"""print("outside the block y :",y)"""


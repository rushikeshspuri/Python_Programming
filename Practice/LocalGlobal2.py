no = 11         # Global variable

def Display():
    a = 21      # Local variable
    print("from Display : ",no)
    print("From display value of a : ",a)
    

def Demo():
    print("from Demo : ",no)
    print("From Demo value of a : ",a)   # interpreter error

Display()
Demo()
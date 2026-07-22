
    
def main():
    try:
        fobj = open("demo.txt",'r')
    
        Data = fobj.read()
    
        print(Data)
        print(type(Data)) 
        
    except FileNotFoundError as fobj:
        print("FILE NOT FOUND")
    
if __name__ == "__main__":
    main()
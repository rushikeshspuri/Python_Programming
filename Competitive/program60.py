def Countline(file):            # Define a function that accepts a file name as a parameter.
    iCount = 0                  # created  a iCount for counting the lines

    try:                        # Try to execute the file operations. If an exception occurs,
                                # control moves to the except block.
        
        fobj = open(file,'r')   # open the file in read mode

        Data = fobj.readlines() # use readlines() method to read the whole lines not char 

        for x in Data:          # Iterate through each line in the list.
            iCount+=1           # while the lines get added in x the counter will increment by 1
               
        return iCount           # after that returning iCount
    except FileNotFoundError as fobj:
        print("FILE NOT FOUND")

    fobj.close()
    
def main():
    Name = input("Enter file name \n")      # taking input file Name

    Ret = Countline(Name)                   # calling the Countline(Name) 

    print(Ret)                              # printing the total number of count

if __name__ == "__main__":
    main()
class Arithmetic:
    def Addition(self,No1,No2):
        Ans = No1 + No2
        return Ans

    def Subtraction(self,No1,No2):
        Ans = No1 - No2
        return Ans
    
aobj = Arithmetic ()

print("Enter first Number")
value1 = int(input())

print("Enter second Number")
value2 = int(input())

# Ret = Addition(aobj,value1,value2)  
Ret = aobj.Addition(value1,value2)      
print("Addition is : ",Ret)

# Ret = Subtraction(aobj,value1,value2)  
Ret = aobj.Subtraction(value1,value2)   
print("Subtraction is : ",Ret)

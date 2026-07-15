class Arithmetic:
    def Addition(No1,No2):
        Ans = No1 + No2
        return Ans

    def Subtraction(No1,No2):
        Ans = No1 - No2
        return Ans
    
aobj = Arithmetic ()

print("Enter first Number")
value1 = int(input())

print("Enter second Number")
value2 = int(input())

Ret = aobj.Addition(value1,value2)      #Error
print("Addition is : ",Ret)

Ret = aobj.Subtraction(value1,value2)   #Error
print("Subtraction is : ",Ret)

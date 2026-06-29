def ChkVowel(ch):
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'or 
       ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'u'):
       return True
    else:
        return False
    
def main():
    print("Enter Character")
    Value = input()

    Ret = ChkVowel(Value)

    if(Ret == True):
        print("It is Vowel")
    else:
        print("It is no vowel")


if __name__ == "__main__":
    main()
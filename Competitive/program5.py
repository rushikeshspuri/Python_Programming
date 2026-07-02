def Display(Name , Age):
    print(f"Hello {Name}, you will turn {Age + 1} next year")


def main():
    name = input("Enter your name\n")
    age = int(input("Enter your age\n"))
    Display(name , age)

main()

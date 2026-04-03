import random


def bigNumber(a,b):
    if a > b:
        print("big number: ", a)
    elif a < b:
        print("big number: ", b)
    else:
        print("both numbers are equal")

def main():
    number1 = int(input("enter first number: "))
    number2 = int(input("enter second number: "))
    bigNumber(number1,number2)



if __name__ == "__main__":
    main()






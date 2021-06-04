def add(num1, num2):
    print (num1+num2)


def minus(num1, num2):
    print (num1-num2)


def multiply(num1,num2):
    print(num1*num2)

def divide(num1,num2):
    print(num1/num2)

def get_input():
    num1 = input("Enter num1: ")
    #print(num1)
    num2 = input("Enter num2: ")
    #print(num2)
    operation=input("Which method do you want to perform.\nThe options are 1 for add, 2 for minus, 3 for multiply, and 4 for divide: ")
    if operation=="1":
        add(int(num1),int(num2))
    elif operation=="2":
        minus(int(num1),int(num2))
    elif operation=="3":
        multiply(int(num1),int(num2))
    elif operation=="4":
        divide(int(num1), int(num2))
    else:
        print(f"{operation} is not a valid operation, the valid options are 1, 2, 3, 4")



get_input()








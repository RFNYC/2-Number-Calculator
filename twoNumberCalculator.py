print("Hello User1. What operation would you like to perform?")

#This variable serves as a box that saves whatever function the calculator is told to perform.
operation = input("Desired Operation: ")

#Each def statement adds a function to the calculator. 
#calling the addition function in the future will add two given numbers because its defined here for example.
def addition(num1, num2):
    print(float(num1)+float(num2))
def subtraction(num1, num2):
    print(float(num1)-float(num2))
def multiplication(num1, num2):
    print(float(num1)*float(num2))
def division(num1, num2):
    print(float(num1)/float(num2))

'''
 This states that if whats inside our box matches either of the given strings matches, the calc will ask the user for two numbers.
 After asking for two numbers it will carryout the corresponding operation.

 If whatever the user saved in our box is not an operation defined or is improperly spelled the calculator will tell the user
 that the operation they chose is invalid.
'''
if operation in ["addition","add"]:
    num1 = input("Insert number 1: ")
    num2 = input("Insert number 2: ")
    addition(num1, num2)
elif operation in ("subtraction","subtract"):
    num1 = input("Insert number 1: ")
    num2 = input("Insert number 2: ")
    subtraction(num1,num2)
elif operation in ("multiplication","multiply"):
    num1 = input("Insert number 1: ")
    num2 = input("Insert number 2: ")
    multiplication(num1,num2)
elif operation in ("division","divide"):
    num1 = input("Insert number 1: ")
    num2 = input("Insert number 2: ")
    division(num1,num2)
else:
    print("Invalid operation.")

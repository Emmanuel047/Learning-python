#Basic Calculator
#Create a basic calculator that can perform 
# addition, subtraction, 
# multiplication, and division. Y
# You can add more operations as you advance.
import time
print("Hi there this is a simple calculator")
choice = ["1", "2", "3", "4", "q"]

while True:
    operation = input("""Choose your operation:\n"""
                      """1. Addition.\n""" 
                      """2. Subtraction.\n"""
                      """3. Multiplication.\n"""
                      """4. Division.\n"""
                      """Q. For exit.\n""").lower()
    if operation in choice :
        break
    print("\nEnter a valid choice\n")
print("You chose: ", operation)    
if operation == "q":
    print("Exiting calculator...")
    time.sleep(0.5)# import time
    exit()
num1 = int(input("Enter a num: "))
num2 =  int(input("Enter a num: "))

def sum(a, b):
    return a + b

def minus(a, b):
    return a - b

def Multiply(a, b):
    return a * b

def Division(a , b):
    if b == 0:
        return "Error division by zero is not allowed"
    return a / b

if operation == "1":
    result = sum(num1, num2)
elif operation == "2":
    result = minus(num1, num2)
elif operation == "3":
    result = Multiply(num1, num2)
elif operation == "4":
    result = Division(num1, num2)
print(result)

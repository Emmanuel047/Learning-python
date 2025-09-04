#A division program to check for division and practise error handling
#Write a Python program that:

#Asks the user to input two numbers for division.

#Uses a try-except block to:

#Catch ValueError if the inputs are not valid numbers and print a friendly message.

#Catch ZeroDivisionError if the user attempts to divide by zero and print a warning.

#Prints the division result if there are no exceptions.

#Use an else block to confirm successful division.

#Use a finally block to print a message saying "Thank you for using the division program".

try:
    num1 = float(input("Enter the first number: \n"))
    if num1 <= 0:
        raise ValueError("Enter a positive number\n")
except ValueError as e:
    print(f"Enter a valid number {e}\n")
else:
    print(f"You've entered: {num1}\n")

try:
    num2 = float(input("Enter a second number: "))
    if num2 <= 0:
        raise ValueError("Enter a number greater than zero\n")
except ValueError as e:
    print("Enter a valid number {e}\n")
else:
    print(f"Youve entered {num2}\n")

try:
    result = num1 / num2
except ZeroDivisionError as e:
    print(f"Division by zero is not allowed {e}\n")
else:
    print(f"The result of {num1} divided by {num2} is {result}\n")
    print("Division successful!")
finally:
    print("Thanks for using the division program.")
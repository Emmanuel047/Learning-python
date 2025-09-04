#Exercise: Basic Withdrawal Simulator (without classes)
#Ask the user to input their wallet balance (float).

#Ask the user to input an amount they want to withdraw.

#Use a try-except block to:

#Catch invalid number inputs (ValueError).

#Check if withdrawal amount is more than balance. If so, print a friendly error message but don’t use custom exceptions.

#If withdrawal is valid, print the new balance.

#Use finally to print a thank-you message.
import time
try:
    balance = float(input("Enter your wallet balance: "))
    if balance < 0:
        raise ValueError("Balance cant be negative")
    if balance == 0:
        print("Your balance is 0, you cant withdraw annything\n")
        exit()
except ValueError as e:
    print(f"Enter a valid number: {e}\n")
else:
    print(f"You've entered your balance as {balance}\n")

try:
    withdraw_amount = float(input("Enter the amount you wish to withdraw: "))
    if withdraw_amount == 0:
        exit()
    if withdraw_amount < 0:
        raise ValueError("Withdraw amount cant be negative")
    if withdraw_amount > balance:
        time.sleep(1)
        print("The Withdrawal cant continue due to Insufficient Balance\n")
        exit()
    else:
        if  withdraw_amount == balance:
            print("You are withdrawing all your balance!\n")
            time.sleep(1)
        if withdraw_amount < balance:
            new_balance = balance - withdraw_amount
            
except ValueError as e:
    print(f"Enter a valid withdrawal amount {e} \n")
else:
    print(f"After withdrawing {withdraw_amount} your balance is {new_balance} \n")
finally:
    print("Thank you for using our service")
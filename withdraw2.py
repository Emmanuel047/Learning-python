#Create a function to read and validate balance.

#Create a function to perform withdrawal logic with error handling.

#Create a main driver function to run the flow, calling these smaller functions.
import time
def balance():
    while True:
        try:
            bal = float(input("Enter your balance: \n"))
            if bal < 0:
                raise ValueError("Balance cant be negative")
        except ValueError as e:
            print(f"Enter  a valid number {e}\n")
        else:
            print(f"Your balance is {bal}\n")
            return bal
def withdrawal(balance):
    while True:
        try:
            amt = float(input("Enter the amount you wish to withdraw: \n"))
            if amt < 0:
                print("Enter a positive amount\n")
                continue
            if amt > balance:
                print("Insufficient Balance\n")
                continue
        except ValueError as e:
            print(f"Enter a valid amount {e}")
        else:
            print(f"You are withdrawing {amt}")
            return amt
    
def main():
    bal = balance()
    if bal is None:
        print("INvalid input Exiting")
        return
    wdr = withdrawal(bal)
    if wdr is None:
        print("The operation couldn't completed due to invalid input")
        return
    new_balance = bal - wdr
    print(f"After withdrawing {wdr} your new balance is {new_balance}")
    print("Thanks for using our service.")

if __name__ == "__main__":
    main()
#Error handling in python

try:
    num  = int(input("Enter a number: "))
except ValueError as e:
        print(f"Not an integer {e}")
else:
    print(f"You entered: {num}")
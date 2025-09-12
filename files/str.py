emma = input("Enter your name: ").lower()
if  not  isinstance (emma, str):
    raise TypeError("Input must be a string")
emma += ".json"
print(emma)
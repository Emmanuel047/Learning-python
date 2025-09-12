#Learning file operations in python
#Creating a new file and writing to it
#w for writing
with open("sample.txt", "w") as file:
    file.write("Hello its me emma again.")
    
#Appending to an existing file
# a for appending
with open("sample.txt", "a") as file:
    file.write("\nI am appending this line.")
    
    
#function to open and read a file    
def file_opener():
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
        
file_opener()
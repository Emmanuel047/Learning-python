#Learning file operations in python
#Creating a new file and writing to it
#w for writjng
with open("sample.txt", "w") as file:
    file.write("Hello world\n")
    file.write("Hi its me emma\n")
#r for reading
with  open("sample.txt", "r") as file:
    content = file.read()
    print(content)

#appending to a file

with open("sample.txt", "a") as file:
    file.write("Hi i appended this text\n")

with open("sample.txt", "r") as file:
    content = file.read
    print(content)
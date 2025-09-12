#Certainly! Here is the logical approach to building a palindrome checker:

#Input: Take a string input from the user.

##Preprocessing:

#Convert the string to a consistent case (e.g., all lowercase) 
# to ensure the check is case-insensitive.

#Optionally, remove any non-alphanumeric characters (spaces, punctuation)
# if you want to check phrases or sentences.

#Comparison:

#Reverse the processed string.

#Compare the original processed string with the reversed string.

#Decision:

#If both strings are equal, the input is a palindrome.

#Otherwise, it is not.

#Output: Display an appropriate message indicating whether the input is a palindrome or not.
import time
print("Hi welcome to the palindrome checker")

def is_palindrome(s):
    return s == s[::-1]

emma = input("Enter a string: ").lower()
if emma.isalpha():
    is_palindrome(emma)
    if is_palindrome(emma):
        time.sleep(0.5)
        print(f"{emma} is a palindrome")
    else:
        time.sleep(0.5)
        print(f"{emma} is not a palindrome")
else:
    print("String must only contain letters")

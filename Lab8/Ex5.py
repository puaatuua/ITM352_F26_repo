# Create an algorithm that determines whether a string entered by the user is a palindrome 
# (that is, the string is the same when read forwards or backwards). 

# Name: Ava Puaatuua
# Date: Oct. 14, 2026

is_it = "madamImadam"

def is_palindrome(text):
    return text == text[::-1] # Compare the original string to its reverse

if is_palindrome(is_it):
    print(f"{is_it} is a palindrome.")
else:
    print(f"{is_it} is not a palindrome.")

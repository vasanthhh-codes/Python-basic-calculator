def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Example usage
text = input("Enter a string: ")
if is_palindrome(text):0 
    print("Palindrome")
else:
    print("Not a palindrome")
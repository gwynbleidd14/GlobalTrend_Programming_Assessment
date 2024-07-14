'''
9. Write a Python function that generates a random password. The password should
contain a mix of uppercase letters, lowercase letters, digits, and special characters.
'''

import random
import string

def generate(length):
    if length < 8:
        return "An error occurred. Length should be 8 or more characters."
    
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    pwd = ''.join(random.choice(chars) for _ in range(length))
    print("Pasword is: ", pwd)

l = int(input("Enter password length: "))
print(generate(l))    
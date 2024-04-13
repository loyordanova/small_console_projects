import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

password_length = 12

password = ''
for i in range(password_length):
  password += ''.join(secrets.choice(alphabet))

print(password)


"""
1. First step -> import the secrets module.

- The secrets the module has several built-in functions that let you do the following:
* Generate sequences of random numbers that are secure for cryptographic applications.
* Use functions like choice(), randbits(), and randbelow() to generate secure random numbers.
* Generate tokens for a password reset, temporary URLs, and more.

----------------------------------------------------------------

2. Second step -> import string module

-The string module provides string constants that we can use to define the alphabet. We’ll use the following string constants:
* The ascii_letters is a concatenation of letters lowercase and uppercase letters.
* The digits constant is the string containing the numbers 0 to 9: '0123456789'.
* The punctuation constant is the string of all special characters.

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

----------------------------------------------------------------

3. Concatenate the above string

alphabet = letters + digits + special_chars

----------------------------------------------------------------

4. Fix the length

password_length = 12

----------------------------------------------------------------

5. Generate the password

password = ''
for i in range(password_length):
  pwd += ''.join(secrets.choice(alphabet))

print(password)
"""

 import random
import string
def password_generator(length):
    letters=string.ascii_letters
    digits=string.digits
    character=string.punctuation
    all_character=letters+digits+character
    password=''.join(random.choice(all_character)for i in range(length))
    return password
length=int(input("Enter the length of the password:"))  
password = password_generator(length)
print("Generated Password:", password)
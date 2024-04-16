# movieName.py
# Name: Zaphod Beeblebrox (Harsh Shah, Ian Cunningham, and Elizabeth Stapleton)
# email: shahh4@mail.uc.edu, stapleet@mail.uc.edu, cunninig@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 04/23/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment:
# Anything else that's relevant: Used worked done in class and ChatGPT as a reference. 

from cryptography.fernet import Fernet

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    print("Decrypted message:", decrypted_message.decode())


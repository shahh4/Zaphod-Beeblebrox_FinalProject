# main.py
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
    return decrypted_message.decode()

# Your encrypted message
encrypted_message = b"gAAAAABlTNM6SYMj08VEVzQj-dHanJNF3F9TMViW7Tv1EBvvX9R5w7U4ThTMMz1qEaaUQt_hLAc3SHuZe4K197Nfq1aZjrHdig=="

# Your key (replace 'your_key_here' with the actual key)
key = b'r0J5NgEGqsxufa0af1zLpy8DaNhQ9C9ur6PBWqialy4='

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, key)
print("Decrypted message:", decrypted_message)
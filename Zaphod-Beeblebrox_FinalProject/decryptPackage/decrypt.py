# main.py
# Name: Zaphod Beeblebrox (Harsh Shah, Ian Cunningham, and Elizabeth Stapleton)
# email: shahh4@mail.uc.edu, stapleet@mail.uc.edu, cunninig@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 04/23/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: This decrypts a file
# Anything else that's relevant: Used worked done in class and ChatGPT as a reference. 
import json


def decrypt_location(encrypted_data_path, english_text_path):
    with open(encrypted_data_path, 'r') as f:
        encrypted_data = json.load(f)
    
    with open(english_text_path, 'r') as f:
        english_text = f.readlines()
    
    decrypted_location = ""
    
    # Check only for Zaphod Beeblebrox
    if "Zaphod Beeblebrox" in encrypted_data:
        indices = encrypted_data["Zaphod Beeblebrox"]
        decrypted_location += "Zaphod Beeblebrox: "
        for index in indices:
            try:
                index = int(index)
                decrypted_location += english_text[index].strip() + " "
            except ValueError:
                print(f"Skipping invalid index for Zaphod Beeblebrox: {index}")
        decrypted_location += "\n"
    
    print("Decrypted location:\n", decrypted_location.strip())
'''
# Define the variables
encrypted_data_path = "../mainPackage/EncryptedGroupHints.json"
english_text_path = "UCEnglish.txt"
encrypted_message = b"gAAAAABlTNM6SYMj08VEVzQj-dHanJNF3F9TMViW7Tv1EBvvX9R5w7U4ThTMMz1qEaaUQt_hLAc3SHuZe4K197Nfq1aZjrHdig=="
key = b'r0J5NgEGqsxufa0af1zLpy8DaNhQ9C9ur6PBWqialy4='

# Call the functions
location_result = decrypt_location(encrypted_data_path, english_text_path)
print(location_result)
decrypt_message(encrypted_message, key)
'''


'''

def decrypt_location(encrypted_data_path, english_text_path):
    with open(encrypted_data_path, 'r') as f:
        encrypted_data = json.load(f)
    
    with open(english_text_path, 'r') as f:
        english_text = f.readlines()
    
    decrypted_location = ""
    
    for name, indices in encrypted_data.items():
        decrypted_location += f"{name}: "
        for index in indices:
            try:
                index = int(index)  #- 1
                decrypted_location += english_text[index].strip() + " "
            except ValueError:
                print(f"Skipping invalid index for {name}: {index}")
        decrypted_location += "\n"
    
    print("Decrypted location:\n", decrypted_location.strip())
'''


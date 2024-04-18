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
    '''
        Load an image file from disk
        @args: encrypted_data_path (str): The file path to the encrypted data file. 
        english_text_path (str): The file path to the English text file used for decryption.
        @return: none
    '''
    
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

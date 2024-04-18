# main.py
# Name: Zaphod Beeblebrox (Harsh Shah, Ian Cunningham, and Elizabeth Stapleton)
# email: shahh4@mail.uc.edu, stapleet@mail.uc.edu, cunninig@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 04/23/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment:
# Anything else that's relevant: Used worked done in class and ChatGPT as a reference. 

from decryptPackage.decrypt import *
from moviePackage.movieName import *
from imagePackage.image import *

if __name__ == "__main__":
    # Define the variables
    encrypted_data_path = "../mainPackage/EncryptedGroupHints.json"
    english_text_path = "UCEnglish.txt"
    encrypted_message = b"gAAAAABlTNM6SYMj08VEVzQj-dHanJNF3F9TMViW7Tv1EBvvX9R5w7U4ThTMMz1qEaaUQt_hLAc3SHuZe4K197Nfq1aZjrHdig=="
    key = b'r0J5NgEGqsxufa0af1zLpy8DaNhQ9C9ur6PBWqialy4='
    
    # Call the functions
    decrypt_location(encrypted_data_path, english_text_path)
    decrypt_message(encrypted_message, key)
    
    my_image = load_image("../imagePackage/fight_club.jpg")
    my_image.show()
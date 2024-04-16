import json

def decrypt_location(encrypted_data_path, english_text_path):
    # Read encrypted data from JSON file
    with open(encrypted_data_path, 'r') as f:
        encrypted_data = json.load(f)
    
    # Read English text file
    with open(english_text_path, 'r') as f:
        english_text = f.readlines()
    
    decrypted_string = ""
    
    # Iterate through each index in the encrypted data
    for index in encrypted_data:
        # Convert index to integer and subtract 1 (to adjust for 0-based indexing)
        index = int(index) - 1
        # Append the word from English text file corresponding to the index
        decrypted_string += english_text[index].strip() + " "
    
    # Return the decrypted string
    return decrypted_string.strip()

# Example usage:
encrypted_data_path = "EncryptedGroupHints.json"
english_text_path = "UCEnglish.txt"
decrypted_location = decrypt_location(encrypted_data_path, english_text_path)
print("Decrypted location:", decrypted_location)

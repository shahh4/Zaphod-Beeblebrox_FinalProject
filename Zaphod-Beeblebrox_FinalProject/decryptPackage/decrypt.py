import json

def decrypt_location(encrypted_data_path, english_text_path):
    # Read encrypted data from JSON file
    with open(encrypted_data_path, 'r') as f:
        encrypted_data = json.load(f)
    
    # Read English text file
    with open(english_text_path, 'r') as f:
        english_text = f.readlines()
    
    decrypted_location = ""
    
    # Iterate through each name in the encrypted data
    for name, indices in encrypted_data.items():
        decrypted_location += f"{name}: "
        # Iterate through each index for the current name
        for index in indices:
            try:
                # Convert index to integer and subtract 1 (to adjust for 0-based indexing)
                index = int(index) - 1
                # Append the word from English text file corresponding to the index
                decrypted_location += english_text[index].strip() + " "
            except ValueError:
                # If the index is not a valid integer, skip it
                print(f"Skipping invalid index for {name}: {index}")
        decrypted_location += "\n"
    
    # Return the decrypted location
    return decrypted_location.strip()

# Example usage:
encrypted_data_path = "EncryptedGroupHints.json"
english_text_path = "UCEnglish.txt"
decrypted_location = decrypt_location(encrypted_data_path, english_text_path)
print("Decrypted location:\n", decrypted_location)

import random
import string

# Combine space, punctuation, digits, and letter characters into a single string
chars = " " + string.punctuation + string.digits + string.ascii_letters
# Convert the string of characters into a list for easier manipulation
chars = list(chars)
# Copy the characters list to use as a key for encryption
key = chars.copy()

# Shuffle the key list to randomize the order of characters for encryption
random.shuffle(key)

# Encryption Process

# Prompt user for a message to encrypt
original = input("What do you want to encrypt: ")
encrypted = ""  # Initialize an empty string to hold the encrypted message

# Iterate through each letter in the original message
for letter in original:
    index = chars.index(letter)  # Find the index of the letter in the original character list
    encrypted += key[index]  # Use the same index on the shuffled key to encrypt the letter

# Display the original and encrypted messages
print(f"Original Message: {original}")
print(f"Encrypted Message: {encrypted}")

# Decryption Process

# Prompt user for a message to decrypt
encrypted = input("What do you want to decrypt: ")
original = ""  # Initialize an empty string to hold the decrypted message

# Iterate through each letter in the encrypted message
for letter in encrypted:
    index = key.index(letter)  # Find the index of the letter in the shuffled key
    original += chars[index]  # Use the same index on the original character list to decrypt the letter

# Display the encrypted and original messages
print(f"Encrypted Message: {encrypted}")
print(f"Original Message: {original}")

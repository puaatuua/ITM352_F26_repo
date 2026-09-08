# This is a simple Python script to demonstrate the use of the cryptography library for 
# symmetric encryption and decryption using the Fernet module.

# Name: Ava Puaatuua
# Date: September 8, 2026

# Import the excryption class
# Fernet is a symmetric encryption tool from the cryptography library
from cryptography.fernet import Fernet

# Generate a unique secret key for encryption and decryption
key = Fernet.generate_key()
# Create a cipher object using the generated key
cipher_suite = Fernet(key)

# Encrypts the string "Hello, World!" and prints the encoded text
encoded_text = cipher_suite.encrypt(b"Hello, World!")
print("Encoded_text: ", encoded_text)

# Reverse the encryption
decoded_text = cipher_suite.decrypt(encoded_text)
print("Decoded_text: ", decoded_text)
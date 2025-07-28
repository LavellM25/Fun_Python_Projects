# Encrypted message using a Caesar cipher with a shift of 5
encrypted_message = "HTSLWFYZQFYNTSX DJW QJFWSNSL UDYMTS"

# The number of positions each letter was shifted forward to encrypt it
shift = 5

# We will build the decrypted message one character at a time
decrypted_message = ""

# Loop through each character in the encrypted message
for char in encrypted_message:

    # If the character is a space, keep it as a space
    if char == " ":
        decrypted_message += " "

    # If the character is a letter (A–Z)
    elif char.isalpha():
        # Convert the character to its ASCII number
        shifted = ord(char) - shift  # Shift the character back by 5

        # If shifting back goes past 'A', wrap around to the end of the alphabet
        if shifted < ord('A'):
            shifted += 26  # Wrap around using modulo logic

        # Convert the ASCII number back to a character and add it to the result
        decrypted_message += chr(shifted)

    # If it's not a letter or space (e.g., punctuation), add it unchanged
    else:
        decrypted_message += char

# Print the final decrypted message
print(decrypted_message)

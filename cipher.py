def caesar_cipher(text, shift, direction):
    """
    Encrypts or decrypts a text message using the Caesar Cipher technique.

    :param text: The text to be encrypted or decrypted.
    :param shift: The number of positions each character in the text is shifted.
    :param direction: The direction of the shift ('encrypt' or 'decrypt').
    :return: The encrypted or decrypted text.
    """
    if direction == 'decrypt':
        shift = -shift

    cipher_text = ''
    for char in text:
        # Encrypt/decrypt only alphabetic characters
        if char.isalpha():
            # Shift character and wrap if necessary, maintaining case
            shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            cipher_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            cipher_text += char

    return cipher_text

def main():
    print("Caesar Cipher Program")
    direction = input("Do you want to encrypt or decrypt? Type 'encrypt' or 'decrypt': ").lower()
    if direction not in ['encrypt', 'decrypt']:
        print("Invalid option. Please type 'encrypt' or 'decrypt'.")
        return

    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (number): "))

    result = caesar_cipher(text, shift, direction)
    action = "Encrypted" if direction == 'encrypt' else "Decrypted"
    print(f"{action} message: {result}")

if __name__ == "__main__":
    main()

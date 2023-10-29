def caesar_cipher(text, shift, decrypt=False):
    result = ''
    for char in text:
        if char:
            # Determine whether to encrypt or decrypt
            if decrypt:
                shift = -shift
            # Apply the shift
            shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26) + ord('a' if char.islower() else 'A'))
            result += shifted_char
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Choose an option (E)ncrypt or (D)ecrypt (Q to quit): ").upper()
        
        if choice == 'Q':
            break
        elif choice in ['E', 'D']:
            text = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'E':
                encrypted_text = caesar_cipher(text, shift)
                print("Encrypted message:", encrypted_text)
            else:
                decrypted_text = caesar_cipher(text, shift, decrypt=True)
                print("Decrypted message:", decrypted_text)
        else:
            print("Invalid choice. Please enter 'E' for Encrypt, 'D' for Decrypt, or 'Q' to quit.")

if __name__ == "__main__":
    main()
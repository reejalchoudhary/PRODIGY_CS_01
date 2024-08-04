def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if mode == 'decrypt':
                shift_amount = -shift_amount
            
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char

    return result

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (enter 'q' to quit): ").lower()
        if choice == 'q':
            break
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice, please choose 'encrypt', 'decrypt', or 'q' to quit.")
            continue
        
        text = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        
        if choice == 'encrypt':
            encrypted_message = caesar_cipher(text, shift, mode='encrypt')
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'decrypt':
            decrypted_message = caesar_cipher(text, shift, mode='decrypt')
            print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()

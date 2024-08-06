def encrypt(text, shift):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice.lower() == 'e':
        print("Encrypted message:", encrypt(message, shift))
    elif choice.lower() == 'd':
        print("Decrypted message:", decrypt(message, shift))
    else:
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()

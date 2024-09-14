import os
import random
import string
from pystyle import Colorate, Colors

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ascii_art():
    ascii_art = """
    ██╗  ██╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     
    ██║ ██╔╝╚══███╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
    █████╔╝   ███╔╝        ██║   ██║   ██║██║   ██║██║     
    ██╔═██╗  ███╔╝         ██║   ██║   ██║██║   ██║██║     
    ██║  ██╗███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗
    ╚═╝  ╚═╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                           
                    KZ Crypto Tool by dataexe
    """
    print(Colorate.Horizontal(Colors.green_to_cyan, ascii_art))

def display_menu():
    menu = """
    ╔════════════════════════════════╗
       Discord: dataexe
       GitHub: github.com/dataexepy
    ╚════════════════════════════════╝
    
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
      [1] Encrypt a message
      [2] Decrypt a message
      [3] EXIT
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
    print(Colorate.Horizontal(Colors.green_to_cyan, menu))

def create_encryption_map():
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    encrypted_characters = ''.join(random.sample(characters, len(characters)))
    return str.maketrans(characters, encrypted_characters), str.maketrans(encrypted_characters, characters)

def enhanced_encrypt(plain_text, encryption_map):
    return plain_text.translate(encryption_map)

def enhanced_decrypt(cipher_text, decryption_map):
    return cipher_text.translate(decryption_map)

def main():
    encryption_map, decryption_map = create_encryption_map()

    while True:
        clear_terminal()
        display_ascii_art()
        display_menu()

        choice = input(Colorate.Horizontal(Colors.green_to_cyan, "\nkz@crypto:~$ ")).strip()

        if choice == "1":
            message = input(Colorate.Horizontal(Colors.green_to_cyan, "\nEnter the message to encrypt: "))
            encrypted = enhanced_encrypt(message, encryption_map)
            print(Colorate.Horizontal(Colors.green_to_cyan, f"\nEncrypted message: {encrypted}"))

        elif choice == "2":
            message = input(Colorate.Horizontal(Colors.green_to_cyan, "\nEnter the message to decrypt: "))
            decrypted = enhanced_decrypt(message, decryption_map)
            print(Colorate.Horizontal(Colors.green_to_cyan, f"\nDecrypted message: {decrypted}"))

        elif choice == "3":
            print(Colorate.Horizontal(Colors.green_to_cyan, "\nThank you for using KZ Crypto Tool. Goodbye!"))
            break

        else:
            print(Colorate.Horizontal(Colors.red_to_purple, "\nInvalid option. Please try again."))

        input(Colorate.Horizontal(Colors.green_to_cyan, "\nPress Enter to continue..."))

if __name__ == "__main__":
    main()

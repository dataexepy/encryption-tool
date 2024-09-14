import os
import random
import string
import time
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
    print(Colorate.Horizontal(current_color, ascii_art))

def display_menu():
    menu = """
    ╔════════════════════════════════╗
       Discord: dataexe
       GitHub: github.com/dataexepy
    ╚════════════════════════════════╝
    
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
      [1] Encrypt a message
      [2] Decrypt a message
      [3] Change Theme
      [4] Donation Information
      [5] EXIT
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
    print(Colorate.Horizontal(current_color, menu))

def create_encryption_map():
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    encrypted_characters = ''.join(random.sample(characters, len(characters)))
    return str.maketrans(characters, encrypted_characters), str.maketrans(encrypted_characters, characters)

def enhanced_encrypt(plain_text, encryption_map):
    return plain_text.translate(encryption_map)

def enhanced_decrypt(cipher_text, decryption_map):
    return cipher_text.translate(decryption_map)

def choose_theme():
    global current_color
    print(Colorate.Horizontal(Colors.blue_to_white, "\nChoose a theme:"))
    print(Colorate.Horizontal(Colors.blue_to_white, "[1] Green to Cyan"))
    print(Colorate.Horizontal(Colors.blue_to_white, "[2] Purple to Blue"))
    print(Colorate.Horizontal(Colors.blue_to_white, "[3] Red to Yellow"))
    print(Colorate.Horizontal(Colors.blue_to_white, "[4] Blue to White"))
    
    choice = input(Colorate.Horizontal(Colors.blue_to_white, "\nSelect theme (1-4): "))
    
    if choice == "1":
        current_color = Colors.green_to_cyan
    elif choice == "2":
        current_color = Colors.purple_to_blue
    elif choice == "3":
        current_color = Colors.red_to_yellow
    elif choice == "4":
        current_color = Colors.blue_to_white
    else:
        print(Colorate.Horizontal(Colors.red_to_purple, "\nInvalid choice. Defaulting to Green to Cyan."))
        current_color = Colors.green_to_cyan

def display_donation_info():
    donation_info = f"""
╔{'═' * 50}╗
║{' ' * 50}║
║{'🌟 Support KZ Crypto Tool Development 🌟'.center(50)}║
║{' ' * 50}║
╠{'═' * 50}╣
║{' ' * 50}║
║{'Your support helps improve this tool!'.center(50)}║
║{' ' * 50}║
║{'Bitcoin (BTC):'.center(50)}║
║{'bc1q34h0yqqqev59atskc0jszc4q3n9h5mrk73d4mz'.center(50)}║
║{' ' * 50}║
║{'Litecoin (LTC):'.center(50)}║
║{'LXZqfsf2QM1gpNLGPwYqK4tX52d17GL2af'.center(50)}║
║{' ' * 50}║
║{'Thank you for your generosity! 🙏'.center(50)}║
║{' ' * 50}║
╚{'═' * 50}╝
    """
    print(Colorate.Vertical(current_color, donation_info))
    
    # Ajout d'une animation simple
    for _ in range(3):
        print(Colorate.Horizontal(current_color, "\n" + "💖 "*10))
        time.sleep(0.5)
        clear_terminal()
        print(Colorate.Vertical(current_color, donation_info))
        time.sleep(0.5)

def main():
    global current_color
    current_color = Colors.green_to_cyan  # Default theme
    encryption_map, decryption_map = create_encryption_map()

    while True:
        clear_terminal()
        display_ascii_art()
        display_menu()

        choice = input(Colorate.Horizontal(current_color, "\nkz@crypto:~$ ")).strip()

        if choice == "1":
            message = input(Colorate.Horizontal(current_color, "\nEnter the message to encrypt: "))
            encrypted = enhanced_encrypt(message, encryption_map)
            print(Colorate.Horizontal(current_color, f"\nEncrypted message: {encrypted}"))

        elif choice == "2":
            message = input(Colorate.Horizontal(current_color, "\nEnter the message to decrypt: "))
            decrypted = enhanced_decrypt(message, decryption_map)
            print(Colorate.Horizontal(current_color, f"\nDecrypted message: {decrypted}"))

        elif choice == "3":
            choose_theme()

        elif choice == "4":
            display_donation_info()
            input(Colorate.Horizontal(current_color, "\nPress Enter to return to the main menu..."))

        elif choice == "5":
            print(Colorate.Horizontal(current_color, "\nThank you for using KZ Crypto Tool. Goodbye!"))
            break

        else:
            print(Colorate.Horizontal(Colors.red_to_purple, "\nInvalid option. Please try again."))

        if choice != "4":  # Skip this for donation info as it has its own prompt
            input(Colorate.Horizontal(current_color, "\nPress Enter to continue..."))

if __name__ == "__main__":
    main()

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
                                                       
                                           by dataexe | Github: dataexepy
    """
    colored_ascii_art = Colorate.Horizontal(Colors.blue_to_white, ascii_art)
    print(colored_ascii_art)

def create_encryption_map():
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    encrypted_characters = ''.join(random.sample(characters, len(characters)))
    return str.maketrans(characters, encrypted_characters), str.maketrans(encrypted_characters, characters)

def enhanced_encrypt(plain_text, encryption_map):
    return plain_text.translate(encryption_map)

def enhanced_decrypt(cipher_text, decryption_map):
    return cipher_text.translate(decryption_map)

def main():
    clear_terminal()
    display_ascii_art()

    encryption_map, decryption_map = create_encryption_map()

    while True:
        print(Colorate.Horizontal(Colors.blue_to_white, "\n1. Chiffrer une phrase"))
        print(Colorate.Horizontal(Colors.blue_to_white, "2. Déchiffrer une phrase"))
        print(Colorate.Horizontal(Colors.blue_to_white, "3. Quitter"))

        choice = input(Colorate.Horizontal(Colors.blue_to_white, "\nSélectionnez une option: ")).strip()

        if choice == "1":
            phrase = input(Colorate.Horizontal(Colors.blue_to_white, "\nEntrez la phrase a chiffrer: "))
            encrypted = enhanced_encrypt(phrase, encryption_map)
            print(Colorate.Horizontal(Colors.blue_to_white, f"Phrase chiffrée: {encrypted}"))

        elif choice == "2":
            phrase = input(Colorate.Horizontal(Colors.blue_to_white, "\nEntrez la phrase à dechiffrer: "))
            decrypted = enhanced_decrypt(phrase, decryption_map)
            print(Colorate.Horizontal(Colors.blue_to_white, f"Phrase dechiffrée: {decrypted}"))

        elif choice == "3":
            print()
            break

        else:
            print(Colorate.Horizontal(Colors.blue_to_white, "\nOption invalide. Veuillez reessayer."))

        input(Colorate.Horizontal(Colors.blue_to_white, "\nAppuyez sur Entree pour continuer..."))
        clear_terminal()
        display_ascii_art()

if __name__ == "__main__":
    main()

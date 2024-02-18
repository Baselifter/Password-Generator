#
# __________  _____________________
# \______   \/  |  \______  \      \
#  |     ___/   |  |_  /    /   |   \
#  |    |  /    ^   / /    /    |    \
#  |____|  \____   | /____/\____|__  /
#               |__|               \/
# ======================================================================
#	Code by:	Baselifter		Date:   18.02.2023
#	Version: 	1.0				Mail:	project.northstorm@gmail.com
# ----------------------------------------------------------------------
#	License: DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# 				  Copyright (C) 2004 Sam Hocevar
#  			  14 rue de Plaisance, 75014 Paris, France
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# 					  as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  				0. You just DO WHAT THE FUCK YOU WANT TO.
# ----------------------------------------------------------------------

import os
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    chars = ''
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def generate_and_save_passwords(num_passwords, length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
        passwords.append(password)

    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    file_path = os.path.join(desktop_path, 'generated_passwords.txt')

    with open(file_path, 'w') as file:
        for i, password in enumerate(passwords, 1):
            file.write(f"{i}.)\t{password}\n")

def main():
    num_passwords = int(input("Bitte geben Sie die Anzahl der zu generierenden Passwörter ein: "))
    length = int(input("Bitte geben Sie die Länge der Passwörter ein (zwischen 4 und 50 Zeichen): "))

    use_uppercase = input("Großbuchstaben enthalten? (ja/nein): ").lower() == 'ja'
    use_lowercase = input("Kleinbuchstaben enthalten? (ja/nein): ").lower() == 'ja'
    use_numbers = input("Zahlen enthalten? (ja/nein): ").lower() == 'ja'
    use_special_chars = input("Sonderzeichen enthalten? (ja/nein): ").lower() == 'ja'

    if not (use_uppercase or use_lowercase or use_numbers or use_special_chars):
        print("Fehler: Mindestens eine der Optionen Großbuchstaben, Kleinbuchstaben, Zahlen oder Sonderzeichen muss ausgewählt werden.")
        return

    if length < 4 or length > 50:
        print("Fehler: Die Passwortlänge muss zwischen 4 und 50 Zeichen liegen.")
        return

    generate_and_save_passwords(num_passwords, length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
    print(f"{num_passwords} Passwörter wurden generiert und auf dem Desktop gespeichert.")

if __name__ == "__main__":
    main()
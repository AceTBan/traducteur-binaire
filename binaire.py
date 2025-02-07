# Dictionnaire de traduction du texte en Morse
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

# Dictionnaire de traduction du texte en alphabet grec
greek_alphabet_dict = {
    'A': 'Α', 'B': 'Β', 'C': 'Γ', 'D': 'Δ', 'E': 'Ε', 'F': 'Ζ', 'G': 'Η', 'H': 'Θ',
    'I': 'Ι', 'J': 'Κ', 'K': 'Λ', 'L': 'Μ', 'M': 'Ν', 'N': 'Ξ', 'O': 'Ο', 'P': 'Π',
    'Q': 'Ρ', 'R': 'Σ', 'S': 'Τ', 'T': 'Υ', 'U': 'Φ', 'V': 'Χ', 'W': 'Ψ', 'X': 'Ω',
    'Y': 'Α', 'Z': 'Β'
}

def text_to_morse(text):
    """ Convertit le texte en code Morse """
    morse = ' '.join(morse_code_dict.get(char.upper(), '') for char in text)
    return morse

def morse_to_text(morse):
    """ Convertit le code Morse en texte """
    morse_to_char = {v: k for k, v in morse_code_dict.items()}
    text = ''.join(morse_to_char.get(code, '') for code in morse.split(' '))
    return text

def text_to_binary(text):
    """ Convertit le texte en binaire """
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    """ Convertit le binaire en texte """
    binary_values = binary.split(' ')
    text = ''.join(chr(int(b, 2)) for b in binary_values)
    return text

def text_to_hexadecimal(text):
    """ Convertit le texte en hexadécimal """
    hexadecimal = ' '.join(format(ord(char), '02x') for char in text)
    return hexadecimal

def hexadecimal_to_text(hexadecimal):
    """ Convertit l'hexadécimal en texte """
    hex_values = hexadecimal.split(' ')
    text = ''.join(chr(int(h, 16)) for h in hex_values)
    return text

def text_to_greek(text):
    """ Convertit le texte en alphabet grec """
    greek = ''.join(greek_alphabet_dict.get(char.upper(), char) for char in text)
    return greek

def greek_to_text(greek):
    """ Convertit l'alphabet grec en texte """
    greek_to_char = {v: k for k, v in greek_alphabet_dict.items()}
    text = ''.join(greek_to_char.get(char, char) for char in greek)
    return text

def text_to_ascii(text):
    """Convertit le texte en code ASCII"""
    ascii_codes = ' '.join(str(ord(char)) for char in text)
    return ascii_codes

def ascii_to_text(ascii_codes):
    """Convertit le code ASCII en texte"""
    text = ''.join(chr(int(code)) for code in ascii_codes.split())
    return text

def main():
    while True:
        conversion_choice = input("Voulez-vous utiliser le binaire (1), l'hexadécimal (2), le morse (3), l'alphabet grec (4) ou l'ASCII (5) ? Entrez 1, 2, 3, 4 ou 5 (ou 'q' pour quitter) : ")
        
        if conversion_choice == '1':
            direction = input("Voulez-vous traduire du texte en binaire (1) ou du binaire en texte (2) ? Entrez 1 ou 2 : ")

            if direction == '1':
                text = input("Entrez le texte à traduire en binaire : ")
                binary = text_to_binary(text)
                print(f"Texte en binaire : {binary}")
            elif direction == '2':
                binary = input("Entrez le binaire à traduire en texte : ")
                text = binary_to_text(binary)
                print(f"Binaire en texte : {text}")
            else:
                print("Choix invalide. Veuillez entrer 1 ou 2.")
        
        elif conversion_choice == '2':
            direction = input("Voulez-vous traduire du texte en hexadécimal (1) ou de l'hexadécimal en texte (2) ? Entrez 1 ou 2 : ")

            if direction == '1':
                text = input("Entrez le texte à traduire en hexadécimal : ")
                hexadecimal = text_to_hexadecimal(text)
                print(f"Texte en hexadécimal : {hexadecimal}")
            elif direction == '2':
                hexadecimal = input("Entrez l'hexadécimal à traduire en texte : ")
                text = hexadecimal_to_text(hexadecimal)
                print(f"Hexadécimal en texte : {text}")
            else:
                print("Choix invalide. Veuillez entrer 1 ou 2.")
        
        elif conversion_choice == '3':
            direction = input("Voulez-vous traduire du texte en morse (1) ou du morse en texte (2) ? Entrez 1 ou 2 : ")

            if direction == '1':
                text = input("Entrez le texte à traduire en morse : ")
                morse = text_to_morse(text)
                print(f"Texte en morse : {morse}")
            elif direction == '2':
                morse = input("Entrez le morse à traduire en texte : ")
                text = morse_to_text(morse)
                print(f"Morse en texte : {text}")
            else:
                print("Choix invalide. Veuillez entrer 1 ou 2.")
        
        elif conversion_choice == '4':
            direction = input("Voulez-vous traduire du texte en alphabet grec (1) ou de l'alphabet grec en texte (2) ? Entrez 1 ou 2 : ")

            if direction == '1':
                text = input("Entrez le texte à traduire en alphabet grec : ")
                greek = text_to_greek(text)
                print(f"Texte en alphabet grec : {greek}")
            elif direction == '2':
                greek = input("Entrez l'alphabet grec à traduire en texte : ")
                text = greek_to_text(greek)
                print(f"Alphabet grec en texte : {text}")
            else:
                print("Choix invalide. Veuillez entrer 1 ou 2.")
        
        elif conversion_choice == '5':
            direction = input("Voulez-vous traduire du texte en ASCII (1) ou de l'ASCII en texte (2) ? Entrez 1 ou 2 : ")

            if direction == '1':
                text = input("Entrez le texte à traduire en ASCII : ")
                ascii_codes = text_to_ascii(text)
                print(f"Texte en ASCII : {ascii_codes}")
            elif direction == '2':
                ascii_codes = input("Entrez le code ASCII à traduire en texte : ")
                text = ascii_to_text(ascii_codes)
                print(f"ASCII en texte : {text}")
            else:
                print("Choix invalide. Veuillez entrer 1 ou 2.")
        
        elif conversion_choice == 'q':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer 1, 2, 3, 4, 5 ou 'q'.")

if __name__ == "__main__":
    main()

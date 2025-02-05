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

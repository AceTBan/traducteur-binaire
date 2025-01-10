def text_to_binary(text):
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    binary_values = binary.split(' ')
    text = ''.join(chr(int(b, 2)) for b in binary_values)
    return text

def main():
    choice = input("Voulez-vous traduire des mots en binaire (1) ou du binaire en mots (2) ? Entrez 1 ou 2 : ")
    
    if choice == '1':
        text = input("Entrez le texte à traduire en binaire : ")
        binary = text_to_binary(text)
        print(f"Texte en binaire : {binary}")
    elif choice == '2':
        binary = input("Entrez le binaire à traduire en texte : ")
        text = binary_to_text(binary)
        print(f"Binaire en texte : {text}")
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")

if __name__ == "__main__":
    main()
def text_to_binary(text):
    # Convertit le texte en une chaîne binaire
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    # Convertit la chaîne binaire en texte
    binary_values = binary.split(' ')
    text = ''.join(chr(int(b, 2)) for b in binary_values)
    return text

def main():
    while True:
        # Demande à l'utilisateur de choisir une option
        choice = input("Voulez-vous traduire des mots en binaire (1) ou du binaire en mots (2) ? Entrez 1 ou 2 (ou 'q' pour quitter) : ")

        if choice == '1':
            # Option pour traduire du texte en binaire
            text = input("Entrez le texte à traduire en binaire : ")
            binary = text_to_binary(text)
            print(f"Texte en binaire : {binary}")
        elif choice == '2':
            # Option pour traduire du binaire en texte
            binary = input("Entrez le binaire à traduire en texte : ")
            text = binary_to_text(binary)
            print(f"Binaire en texte : {text}")
        elif choice == 'q':
            # Option pour quitter le programme
            print("Au revoir !")
            break
        else:
            # Message en cas de choix invalide
            print("Choix invalide. Veuillez entrer 1, 2 ou 'q'.")

if __name__ == "__main__":
    main()

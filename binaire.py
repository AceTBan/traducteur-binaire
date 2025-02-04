def text_to_binary(text):
    # Convertit le texte en une chaîne binaire
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    # Convertit la chaîne binaire en texte
    binary_values = binary.split(' ')
    text = ''.join(chr(int(b, 2)) for b in binary_values)
    return text

def text_to_hexadecimal(text):
    # Convertit le texte en une chaîne hexadécimale
    hexadecimal = ' '.join(format(ord(char), '02x') for char in text)
    return hexadecimal

def hexadecimal_to_text(hexadecimal):
    # Convertit la chaîne hexadécimale en texte
    hex_values = hexadecimal.split(' ')
    text = ''.join(chr(int(h, 16)) for h in hex_values)
    return text

def main():
    while True:
        # Demande à l'utilisateur de choisir un type de conversion
        conversion_choice = input("Voulez-vous utiliser le binaire (1) ou l'hexadécimal (2) ? Entrez 1 ou 2 (ou 'q' pour quitter) : ")
        
        if conversion_choice == '1':
            # Choix pour les conversions binaires
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
            # Choix pour les conversions hexadécimales
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
        
        elif conversion_choice == 'q':
            # Option pour quitter le programme
            print("Au revoir !")
            break
        else:
            # Message en cas de choix invalide
            print("Choix invalide. Veuillez entrer 1, 2 ou 'q'.")

if __name__ == "__main__":
    main()

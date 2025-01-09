def text_to_binary(text):
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    binary_values = binary.split(' ')
    text = ''.join(chr(int(b, 2)) for b in binary_values)
    return text
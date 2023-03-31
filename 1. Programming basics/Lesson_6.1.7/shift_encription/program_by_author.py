alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def shift_encode(string):

    string_encoded = ""
    
    for letter in string:
        
        position = alphabet.find(letter)
        position_next = (position+1) % len(alphabet)
        next_letter = alphabet[position_next]
        string_encoded += next_letter
    
    return string_encoded

print(shift_encode("абзац"))


def shift_decode(string):

    string_encoded = ""
    
    for letter in string:
        
        position = alphabet.find(letter)
        position_next = (position-1+33) % len(alphabet)
        next_letter = alphabet[position_next]
        string_encoded += next_letter
    
    return string_encoded

print(shift_decode("бвибч"))

# The Caesar Cipher Encoding and Decoding
from art import logo
print(logo)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
             'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Encrypting the message

def encrypt(text, shift_position):
    cipher_text = ""
    for char in text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift_position
            new_letter = alphabets[new_position]
            cipher_text = cipher_text + new_letter
        else:
            cipher_text = cipher_text + char
    print(f"The encoded text is {cipher_text}")


# Decrypting the message

def decrypt(cipher_text, shift_position):
    original_text = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position - shift_position
            new_letter = alphabets[new_position]
            original_text = original_text + new_letter
        else:
            original_text = original_text + char

    print(f"The decoded text is {original_text}")


should_continue = True
while should_continue:
    direction = input("Enter 'encode' to encrypt and 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift_position = int(input("Enter the shift number: "))

    # if the user enters the shift number greater than no. of letters in alphabet
    shift_position = shift_position % 25

    if direction == "encode":
        encrypt(text, shift_position)
    elif direction == "decode":
        decrypt(cipher_text=text, shift_position=shift_position)

    result = input(
        "Type yes if you want to continue or no if you want to exit: \n")
    if result == "no":
        should_continue = False
        print("Goodbye")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

import art

print(art.logo)


def caesar(input_text, shift_amount, direction):
    cipher_text = ''
    if direction == 'decode':
        shift_amount *= -1
    for char in input_text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift_amount) % 26
            cipher_text += alphabet[new_index]
        else:
            cipher_text += input_text
    print(f"The {direction}d text is: {cipher_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(input_text=text, shift_amount=shift, direction=direction)

    result = input("Type yes for continue encoding or decoding Or no for terminate the program").lower()
    if result == 'no':
        should_continue = False
        print("Good Bye")



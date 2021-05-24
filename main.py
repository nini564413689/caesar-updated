alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == "decode":
        shift *= -1
def caesar (message, keynumber, encode_or_decode):
    final_text = ""
    for letter in message:
        position = alphabet.index (letter)
        cipher_position = position + keynumber
        cipher_letter = alphabet [cipher_position]
        final_text += cipher_letter
    print (f"Here's the {direction}d result: {final_text}")
caesar (message = text, keynumber = shift, encode_or_decode = direction)
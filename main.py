alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar (message, keynumber, encode_or_decode):
        final_text = ""
        for letter in message:
            position = alphabet.index (letter)
            cipher_position = position + keynumber
            if cipher_position > 25 or cipher_position < -26:
                cipher_position %= 26         
            cipher_letter = alphabet [cipher_position]
            final_text += cipher_letter
        print (f"Here's the {direction}d result: {final_text}")


end_of_program = False
while end_of_program == False: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "decode":
            shift *= -1
                   
    caesar (message = text, keynumber = shift, encode_or_decode = direction)
    runagain = input ("Do you want to run the program again? Y or N:\n").lower()
    if runagain == "n":
        end_of_program = True
        print ("Goodbye!!!")
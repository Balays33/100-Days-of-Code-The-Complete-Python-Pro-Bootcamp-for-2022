from art import logo

#print("Caesar Cipher")
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def input_metod():
    code = input("What is the message: ")
    shift_number = int(input("What is the shift number: "))
    return code,shift_number

def encryption(code,shift_number):
    print("encryption")
    print(f"This is the code: {code} and shift number {shift_number}")
    lower_code = code.lower()

    encrypted_code = ""
    for letter in lower_code:
        if letter in alphabet:
            encrypted_code += alphabet[letter]
            
        else:
            encrypted_code += letter
    print(f"This is the encrypted code: {encrypted_code}")
    print(encrypted_code)




def decryption():
    print("decryption")


def codedirection(direction):
    if direction == "encode":
        
        code,shift_number = input_metod()

        encryption(code,shift_number)
    elif direction == "decode":
        input_metod()
        decryption()
    else:
        print("Error")



direction = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n"))
codedirection(direction)



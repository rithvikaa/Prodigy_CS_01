alphabet={chr(i):i-97 for i in range(97,123)}
def caesar_cipher_encrypt(text,shift):
    encrypted_text=""
    for char in text:
        if char.isalpha():
            char_lower=char.lower()
            char_num=alphabet[char_lower]
            shifted_num=(char_num+shift)%26
            encrypted_char=chr(shifted_num+97)if char.islower()else chr(shifted_num+65)
            encrypted_text+=encrypted_char
        else:
            encrypted_text+=char
    return encrypted_text
message=input("Enter your message: ")
shift_value=int(input("Enter the shift value: "))
encrypted_message=caesar_cipher_encrypt(message,shift_value)
print(f"Encrypted message:{encrypted_message}")

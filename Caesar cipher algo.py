alphabet={chr(i):i-97 for i in range(97,123)}
def caesar_cipher(text,shift,mode):
    result=""
    for char in text:
        if char.isalpha():
            char_lower=char.lower()
            char_num=alphabet[char_lower]
            if mode=="encrypt":
                shifted_num=(char_num+shift)%26
            elif mode=="decrypt":
                shifted_num=(char_num-shift)%26
            result+=chr(shifted_num+97)if char.islower()else chr(shifted_num+65)
        else:
            result+=char
    return result

message=input("Enter your message: ")
shift_value=int(input("Enter the shift value: "))
mode=input("Choose mode (encrypt/decrypt): ").lower()
result=caesar_cipher(message,shift_value,mode)
print(f"Result: {result}")

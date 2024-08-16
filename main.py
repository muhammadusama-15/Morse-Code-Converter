# Python program to implement Morse Code Translator
 
# Dictionary representing the morse code chart -- Obtained From Google
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

#Defining functions to encode and decode the message
def encode(message):
    message = message.upper() #Converting into upper case as the dictionary contains only upper case alphabets
    encoded_message = ""
    for character in message:
        encoded_message += MORSE_CODE_DICT.get(character)+" " #Adding a space after each elements encoding because this space is necessary for decoding the message.
    print(f"The encoded message is: {encoded_message}")
    return encoded_message

def decode(encoded_message):
    encoded_message = encoded_message.strip() #For removing last space as it is unnecessary
    encoded_message = encoded_message.split(" ")
    decoded_message = ""
    for character in encoded_message:
        for key,value in MORSE_CODE_DICT.items():
            if value == character:
                decoded_message += key
    print(f"The decoded message is: {decoded_message}")
    return decoded_message


#Welcoming the user
print("------------------------------------------Welcome to Morse Code Converter------------------------------------------")
print("---------------------------------------------Make Your Messages Private--------------------------------------------")
print()

program_is_running = True

while program_is_running:
    #Letting the user decide to encode or decode
    user_input = input("Do you want to 'encode' or 'decode' the message? Type 'exit' to stop the program: ").lower()
    if user_input == "encode":
        message = input("Enter the message to be encoded: ")
        encode(message=message)

    elif user_input == "decode":
        message = input("Enter the message to be decoded: ")
        decode(encoded_message=message)

    elif user_input == "exit":
        program_is_running = False

    else:
        print("Oops! Kindly check the spellings ('encode' for encoding and 'decode' for decoding): ")


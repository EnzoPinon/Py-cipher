# this is the Vigenere Cipher, decoding and encoding with the key.

user_stop = False

# greet the user
print("Welcome to the Vigenere Cipher maker!")

while user_stop == False:

    request_type = str(input("Indicate if this is to encode or decode, or 'stop' to stop the process: "))
    #check if it is to stop
    print(request_type)
    if request_type.lower() == 'stop':
        user_stop = True
        print("Stopping! See you soon!")
        break

    # We break things down into two: Encode and Decode.
    if request_type.lower() == "encode":
        # ask for the string

        message = str(input("Please state the message to encode, no spaces, all caps: "))
        #ask for the key
        key = str(input("Please state the key, no spaces, all caps: "))
    
        # remove spaces
        message_nospace = message.replace(" ", "")
        key_nospace = key.replace(" ", "")

        # all caps

        string_encode = message_nospace.upper()
        encode_key = key_nospace.upper()
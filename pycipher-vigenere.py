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

    
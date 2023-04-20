# this activity will allow encryption and decryption of vowels only.

# define when to stop

user_stop = False

# simple greeting!
print("Hi there! I am PyCipher-Simple! I only encrypt and decrypt vowels.")

while user_stop == False:

    # ask user to input an encrypted statement.
    encrypted = input("Indicate whether you wish to 'encrypt', 'decrypt', or 'stop' the program: ")

     # check if the user wanted to stop

    if encrypted.lower() == "stop":

        #set the initial variable to True to break the loop

        user_stop = True

        # say goodbye!
    
        print("Goodbye and hope to see you again!")

    if encrypted.lower() == "decrypt":
        # ask for word to decrypt
        todecypt = input("You have chosen 'decrypt'! Please type the message to decode.")

        # attempt to replace every encrypted symbol with an appropriate equivalent.
        first_vowel = todecypt.replace('*', 'a')
        second_vowel = first_vowel.replace('&', 'e')
        third_vowel = second_vowel.replace('#', 'i')
        fourth_vowel = third_vowel.replace('+', 'o')
        final_decrypted = fourth_vowel.replace('!', 'u')

        # print the decrypted message in low caps
        print("The encrypted message is: ", todecypt)
        print("The decrypted message is: ", final_decrypted.lower())
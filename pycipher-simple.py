# this activity will allow encryption and decryption of vowels only.

# define when to stop

user_stop = False

# simple greeting!
print("Hi there! I am PyCipher-Simple! I only encrypt and decrypt vowels.")

while user_stop == False:

    # ask user to input an encrypted statement.
    encrypted = input("Input a statement that is already encrypted, or say 'stop' to stop: ")
    
     # check if the user wanted to stop

    if encrypted.lower() == "stop":

        #set the initial variable to True to break the loop

        user_stop = True

        # say goodbye!
    
        print("Goodbye and hope to see you again!")
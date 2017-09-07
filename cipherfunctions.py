# imports
from time import sleep

# well I need the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# ask for function
print("Hey!")
sleep(0.6)
print("So, do you want to (e)ncrypt a string, or (d)ecrypt a string?")

selection = ''


# try block so we can catch a keyboard interrupt
try:

    # pre-define new message
    new_message = ''


    # define the functions
    def encryptstring(messageTOencrypt):

        # encrypt the string
        for character in message:
            encrypted_message = ''
            position = alphabet.find(character)
            new_position = (position + key) % 26
            new_character = alphabet[new_position]
            encrypted_message += new_character
        return encrypted_message

    new_message = ''

    while selection not in ['e', 'd']:
        selection = input("> ")

        if selection == 'e':
            # get the message to cipher
            print("What string do you want to encrypt?")
            sleep(0.2)
            message = input("> ")

            # key for cipher
            print("What do you want the cipher key to be (1-25)?")
            sleep(0.2)
            key = int(input("> "))
            new_message = encryptstring(message)

        elif selection == 'e':
            decryptstring()
        else:
            "You need to enter either 'e' or 'd'..."


        # print everything out
        print('Your encrypted message is', new_message)
        sleep(0.8)
        print("And don't forget your key! (It's", key, "btw)")
        sleep(0.4)

# catch that keyboard interrupt
except KeyboardInterrupt:
    print("Well, see ya later!")

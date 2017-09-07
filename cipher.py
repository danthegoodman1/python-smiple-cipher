# imports
from time import sleep

# well I need the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# ask for function
print("Hey!")
sleep(0.6)
print("So, do you want to (e)ncrypt a string, or (d)ecrypt a string?")

selection = ''

new_message = ''

# check for encryption message to display later
check_enc = 0

# try block so we can catch a keyboard interrupt
try:

    while selection not in ['e', 'd']:
        selection = input("> ")

        if selection == 'e':
            sleep(0.2)
            # get the message to cipher
            print("What string do you want to encrypt?")
            sleep(0.2)
            message = input("> ")

            # key for cipher
            print("What do you want the cipher key to be (1-25)?")
            sleep(0.2)
            key = int(input("> "))

            # pre-define new message
            new_message = ''

            # encrypt the string
            for character in message:
                position = alphabet.find(character)
                new_position = (position + key) % 26
                new_character = alphabet[new_position]
                new_message += new_character

            check_enc = 1

        elif selection == 'd':
            sleep(0.2)
            # get message to decrypt
            print("What message do you want to decrypt?")
            sleep(0.2)
            enc_message = input("> ")

            # key for decryption
            print("What is the key? (1-25)")
            sleep(0.2)
            key = int(input("> "))

            # pre-define new message
            new_message = ''

            # decrypt the string
            for character in enc_message:
                position = alphabet.find(character)
                new_position = (position - key) % 26
                new_character = alphabet[new_position]
                new_message += new_character

        else:
            "You need to enter either 'e' or 'd'..."

    # print everything out
    if check_enc == 1:

        print('Your encrypted message is:', new_message)
        print("And don't forget your key! (It's", key, "btw)")

    elif check_enc == 0:

        print("Your decrypted message is:", new_message)

    else:
        print("WHOA!...")
        sleep(0.4)
        print("Something went REALLY wrong")
        sleep(0.4)
        print("You may want to look the code over")

# catch that keyboard interrupt
except KeyboardInterrupt:
    print("Well, see ya later!")
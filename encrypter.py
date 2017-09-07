# imports
from time import sleep

# try block so we can catch keyboard interrupt
try:
    # well I need the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'


    # get the message to cipher
    print("hello,")
    print("What string do you want to cipher?")
    sleep(0.4)
    message = input("> ")

    # key for cipher
    print("What do you want the cipher key to be (1-25)?")
    sleep(0.4)
    key = int(input("> "))

    # pre-define new message
    new_message = ''

    # encrypt the string
    for character in message:
        position = alphabet.find(character)
        new_position = (position + key) % 26
        new_character = alphabet[new_position]
        new_message += new_character

    # print everything out
    print('Your encrypted message is', new_message)

    print("And don't forget your key! (It's", key, "btw)")

# catch that keyboard interrupt
except KeyboardInterrupt:
    print("Well, see ya later!")
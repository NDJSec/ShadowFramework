import string

alphabet = string.ascii_letters

def decrypt(caesar_cipher, shift):
    msg = list(caesar_cipher)
    emsg = []

    for c in msg:
        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - shift) % 26
            new_character = alphabet[new_position]
            emsg.append(new_character)
        else:
            emsg.append(c)

    message = ''.join(emsg)
    print(message)

def guess(caesar_cipher, flag_start):
    msg = list(caesar_cipher)
    emsg = []
    shift = 1
    message = ''

    while(message.startswith(flag_start.lower()) == False):
        message = ''
    
        for c in msg:
            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position - shift) % 26
                new_character = alphabet[new_position]
                emsg.append(new_character)
            else:
                emsg.append(c)

        decrypted_message = ''.join(emsg)

        
    
        shift += 1
        message = decrypted_message
        emsg.clear()

    print('FLAG:' + decrypted_message)
    print('NOTE: FLAG HAS BEEN CHANGED TO ALL LOWERCASE')
        
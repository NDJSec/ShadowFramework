from shadow.crypto import MD5 
from shadow.crypto import url_encode
from shadow.crypto import caesar
from shadow.crypto  import vignere
import click

class crypto_handler():
    def crypto(self, flag, opt):
        if (flag == 'encrypt'):
            if(opt == '1'):
                str2hash = click.prompt('Please enter a string to be encrypted', type=str)
                print(MD5.encrypt(str2hash))
            if(opt == '2'):
                pass
            if(opt == '3'):
                pass
        if (flag == 'decrypt'):
            if(opt == '1'):
                vignere_cipher = click.prompt('Please enter the cipher to be decrypted', type=str)
                key = click.prompt('Please enter the key length if known.', type=str)
                print(vignere.decrypt(vignere_cipher, key))
                pass
            if(opt == '2'):
                caesar_cipher = click.prompt('Please enter the cipher to be decrypted', type=str)
                shift = click.prompt('Please enter the shift length if known. Press enter to guess the shift', type=int, default=0)
                if(shift != 0):    
                    print(caesar.decrypt(caesar_cipher, shift))
                else:
                    flag_start = click.prompt('Please enter the start of the flag (ex. PicoCTF{)', type=str)
                    print('FLAG:' + caesar.guess(caesar_cipher, flag_start))
                    print('NOTE: FLAG HAS BEEN CHANGED TO ALL LOWERCASE')
            if(opt == '3'):
                pass
        
        
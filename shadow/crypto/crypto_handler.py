from shadow.crypto import MD5 
from shadow.crypto import url_encode
from shadow.crypto import caesar
import click

class crypto_handler():
    def crypto(self, flag, opt):
        if (flag == 'encrypt'):
            if(opt == '1'):
                str2hash = click.prompt('Please enter a string to be encrypted', type=str)
                MD5.encrypt(str2hash)
            if(opt == '2'):
                pass
            if(opt == '3'):
                pass
        if (flag == 'decrypt'):
            if(opt == '1'):
                pass
            if(opt == '2'):
                pass
            if(opt == '3'):
                caesar_cipher = click.prompt('Please enter the cipher to be decrypted', type=str)
                shift = click.prompt('Please eneter the shift length if known. Press enter to guess the shift', type=int, default=0)
                if(shift != 0):    
                    caesar.decrypt(caesar_cipher, shift)
                else:
                    flag_start = click.prompt('Please eneter the start of the flag (ex. PicoCTF{)', type=str)
                    caesar.guess(caesar_cipher, flag_start)
        
        
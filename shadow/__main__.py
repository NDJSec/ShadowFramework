import click
from shadow.networking import cisco_conf
from shadow.crypto import crypto_handler

@click.group()
def shadow():
    '''
    Welcome to the Shadow Framework
    '''

@shadow.command('cisco', short_help='Configure Cisco Equipment')
@click.option('--switch', '-sw', is_flag=True, help="Configure a Switch")
def cisco(switch):
    if(switch):
        ip_addr = click.prompt('Please enter the IP address of the Switch you would like to configure', type=str)
        username = click.prompt('Please enter the Username', type=str)
        passwd = click.prompt('Please enter the Password', type=str, hide_input=True)
        opt = click.prompt('Please choose a configuration option \n' +
        '1: Configure Hostname \n' +
        '2: Configure a Message of the Day \n' +
        '3: Configure passwords \n' +
        '4: Configure VLANs \n' +
        '5: Copy Running Config to Start Config \n' +
        '6: Show Running Config \n' +
        '99: Exit', 
        default='99'
        )

        cisco_conf.connect(ip_addr, username, passwd)
        cisco_conf.config(opt)

@shadow.command('crypto', short_help='Crypto tools')    
@click.option('--encrypt', is_flag=True, help='Encrypt a message')
@click.option('--decrypt', is_flag=True, help='Decrypt a message')
def crypto(encrypt, decrypt):
    if(encrypt):
        opt = click.prompt('Please choose an encryption/encoding type \n' +
        '1: MD5 \n' +
        '2: URL Encode \n' +
        '3: Caesar \n' +
        '4:  \n' +
        '5:  \n' +
        '6:  \n' +
        '99: Exit', 
        default='99'
        )
        crypto_handler.crypto_handler.crypto(None, 'encrypt',opt)
    if(decrypt):
        opt = click.prompt('Please choose an decryption/decoding type \n' +
        '1: Vigenere \n' +
        '2: Caesar \n' +
        '3: Binary \n' +
        '4: Octal \n' +
        '5: Hexadecimal \n' +
        '6: Guess the type \n' +
        '99: Exit', 
        default='99'
        )
        crypto_handler.crypto_handler.crypto(None, 'decrypt',opt)

        

if __name__ == "__main__":
    shadow()
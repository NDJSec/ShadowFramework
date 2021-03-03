def hex_decrypt(hex_input):
    hexdata = bytes(hex_input, 'ascii').decode('ascii')
    hexdata = bytes.fromhex(hexdata).decode('ascii')
    return hexdata
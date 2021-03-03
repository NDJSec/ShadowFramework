def oct_decrypt(oct_input):
    octdata = oct_input.split(' ')
    octdata = ''.join(map(lambda x: chr(int(x, 8)), octdata))
    return(octdata)
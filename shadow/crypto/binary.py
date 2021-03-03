def binary_decrypt(binary):
    binarydata = binary.split(' ')
    binarydata = ''.join(map(lambda x: chr(int(x, 2)), binarydata))
    return(binarydata)
import hashlib

def encrypt(str2hash):
    result = hashlib.md5(str2hash.encode())
    return(result.hexdigest())
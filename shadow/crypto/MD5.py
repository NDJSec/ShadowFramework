import hashlib

def encrypt(str2hash):
    result = hashlib.md5(str2hash.encode())
    print(result.hexdigest())
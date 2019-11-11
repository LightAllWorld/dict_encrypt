from Crypto.Cipher import AES
import pickle
import json


def padding(data):
    return data + b' ' * (16 - (len(data) % 16))


def encryption(plain_txt, key=KEY):
    bytes_from_dict = json.dumps(plain_txt).encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, IV)

    if len(bytes_from_dict) % CHUNK_SIZE != 0:
        bytes_from_dict = padding(bytes_from_dict)
    else:
        pass

    return cipher.encrypt(bytes_from_dict)
    

def decryption(encrypted_data, key=KEY):
    cipher = AES.new(key, AES.MODE_CBC, IV)
    decrypted_data = cipher.decrypt(encrypted_data)

    return json.loads(decrypted_data)
